"""Build a validated local warehouse from the preserved synthetic source files."""
from pathlib import Path
import argparse
import hashlib
import json
import os

import duckdb
import pandas as pd

ROOT = Path(__file__).resolve().parent
DIMENSIONS = {
    'DimDate': ('DimDate/DimDate.csv', 'DateID'),
    'DimLoyaltyProgram': ('DimLoyalty/DimLoyaltyInfo.csv', 'LoyaltyProgramID'),
    'DimCustomer': ('DimCustomer/DimCustomerData.csv', 'CustomerID'),
    'DimProduct': ('DimProduct/DimProductData.csv', 'ProductID'),
    'DimStore': ('DimStore/DimStoreData.csv', 'StoreID'),
}
RENAMES = {
    'First Name': 'FirstName', 'Last Name': 'LastName', 'Phone Number': 'PhoneNumber',
    'Postal Code': 'ZipCode', 'Manager Name': 'ManagerName', 'DayofWeek': 'DayOfWeek',
    'Isweekend': 'IsWeekend', 'QuantityOrderded': 'QuantityOrdered', 'Shipping Cost': 'ShippingCost',
}


def verify_sources():
    """Fail on source changes rather than silently remapping legacy ordinal IDs."""
    manifest = json.loads((ROOT / 'source_manifest.json').read_text())
    for name, expected in manifest.items():
        actual = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
        if actual != expected:
            raise ValueError(f'Source changed: {name}. Review key mapping before updating manifest.')


def prepare_dimensions():
    dimensions = {}
    for table, (file, key) in DIMENSIONS.items():
        df = pd.read_csv(ROOT / 'One Time Load' / file, dtype={'Postal Code': str})
        df = df.rename(columns=RENAMES)
        if key not in df:
            # Adopted convention, not proof of a previous Snowflake load.
            df.insert(0, key, range(1, len(df) + 1))
        dimensions[table] = df
    return dimensions


def prepare_facts(include_landing=False):
    files = [ROOT / 'One Time Load/Fact Orders/factorders.csv']
    if include_landing:
        files += sorted((ROOT / 'Landing Directory').glob('*.csv'))
    parts = []
    for file in files:
        frame = pd.read_csv(file).rename(columns=RENAMES)
        frame['SourceFile'] = str(file.relative_to(ROOT))
        frame['SourceRow'] = range(1, len(frame) + 1)
        parts.append(frame)
    facts = pd.concat(parts, ignore_index=True)
    facts.insert(0, 'OrderID', range(1, len(facts) + 1))
    return facts


def validate(dimensions, facts):
    for table, (_, key) in DIMENSIONS.items():
        df = dimensions[table]
        if df[key].isna().any() or df[key].duplicated().any():
            raise ValueError(f'{table}: invalid primary key')
    for key, table in [('DateID', 'DimDate'), ('CustomerID', 'DimCustomer'),
                       ('ProductID', 'DimProduct'), ('StoreID', 'DimStore')]:
        if not facts[key].isin(dimensions[table][key]).all():
            raise ValueError(f'FactOrders: orphan {key}')
    if not dimensions['DimCustomer'].LoyaltyProgramID.isin(
        dimensions['DimLoyaltyProgram'].LoyaltyProgramID
    ).all():
        raise ValueError('DimCustomer: orphan LoyaltyProgramID')
    if facts.isna().any().any() or facts.OrderID.duplicated().any():
        raise ValueError('FactOrders: null values or duplicate order IDs')
    if (facts.QuantityOrdered <= 0).any() or (facts.OrderAmount < 0).any():
        raise ValueError('FactOrders: invalid quantity or amount')
    residual = facts.TotalAmount - (facts.OrderAmount - facts.DiscountAmount - facts.ShippingCost)
    if residual.abs().max() > 0.000002:
        raise ValueError('FactOrders: amount identity failed')
    return {'fact_rows': len(facts), 'orphan_keys': 0, 'duplicate_order_ids': 0,
            'max_amount_identity_error': float(residual.abs().max())}


def build(include_landing=False, output=None):
    verify_sources()
    output = Path(output or ROOT / 'build')
    output.mkdir(parents=True, exist_ok=True)
    dimensions, facts = prepare_dimensions(), prepare_facts(include_landing)
    quality = validate(dimensions, facts)
    temporary = output / 'warehouse.tmp.duckdb'
    if temporary.exists():
        temporary.unlink()
    con = duckdb.connect(str(temporary))
    try:
        con.execute((ROOT / 'DB Code/DDL.sql').read_text())
        for name, df in {**dimensions, 'FactOrders': facts}.items():
            con.register('input_frame', df)
            con.execute(f'INSERT INTO {name} BY NAME SELECT * FROM input_frame')
            con.unregister('input_frame')
            con.execute(f'SELECT * FROM {name} ORDER BY 1').df().to_csv(output / f'{name}.csv', index=False)
        kpis = con.execute((ROOT / 'sql/kpis.sql').read_text()).df()
        expected = [facts.OrderAmount.sum(), len(facts), facts.CustomerID.nunique(),
                    facts.OrderAmount.mean(), facts.DiscountAmount.sum(), facts.ShippingCost.sum()]
        for actual, reference in zip(kpis.iloc[0], expected):
            if abs(float(actual) - float(reference)) > 0.02:
                raise ValueError('SQL/Pandas KPI reconciliation failed')
        kpis.to_csv(output / 'kpis.csv', index=False, float_format='%.2f')
        con.execute((ROOT / 'sql/store_performance.sql').read_text()).df().to_csv(
            output / 'store_performance.csv', index=False)
        quality['scope'] = 'historical_plus_landing' if include_landing else 'historical_only'
        quality['sql_pandas_kpis_agree'] = True
        (output / 'quality.json').write_text(json.dumps(quality, indent=2) + '\n')
    finally:
        con.close()
    os.replace(temporary, output / 'warehouse.duckdb')
    return quality


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--include-landing', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    print(json.dumps(build(args.include_landing, args.output), indent=2))

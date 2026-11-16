# Retail warehouse modelling and executive KPI preparation

**Synthetic portfolio demonstration.** This repository preserves the original generated data
and adds a reproducible, validated local SQL warehouse. It does not contain client records or
prove business impact. **No native Power BI report is included or claimed.**

## Run

Python 3.10–3.13 recommended. From the repository root:

```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
python pipeline.py
python -m unittest discover -s tests -v
```

The build uses DuckDB locally and requires no cloud credentials. `build/warehouse.duckdb`
and six normalized CSV tables are generated, not committed. Reruns rebuild the local demo
warehouse instead of appending duplicate rows. The final database replaces the old build only
after validation. This is a single-process local build, not a concurrent production loader.

Default scope is the million historical records. To include the separate 51,471-row landing
batch, run `python pipeline.py --include-landing --output build/with_landing`.
Never combine historical and landing KPI outputs without labelling the scope.

## Architecture and grain

Preserved CSVs → normalized columns and explicit keys → constrained SQL tables →
validated KPIs/store rankings → Power BI-ready CSVs and model specification.

One source record represents one synthetic order. Date, Customer, Product and Store link
one-to-many to FactOrders. Loyalty links one-to-many to Customer: a snowflaked loyalty
relationship, not five direct fact relationships. See [DDL](DB%20Code/DDL.sql).

Legacy customer/product/store CSVs lack IDs. This build explicitly adopts 1-based original
source-row positions as their IDs. `source_manifest.json` freezes source identity and prevents
silent remapping if files are reordered or edited. This convention is not proof of prior
Snowflake loading. `SourceFile` and `SourceRow` preserve fact lineage. Historical OrderIDs
remain stable when landing records are included. A changed source requires a reviewed mapping
migration; do not blindly regenerate the manifest.

## Six KPIs

| KPI | Definition |
|---|---|
| Total Sales | Sum of OrderAmount: gross order amount, currency unspecified |
| Total Orders | Distinct OrderID |
| Total Customers | Distinct purchasing CustomerID |
| Average Order Value | Total Sales / Total Orders |
| Total Discount | Sum of DiscountAmount |
| Total Shipping Cost | Sum of ShippingCost |

[SQL](sql/kpis.sql), [executed values](reports/kpis.csv), [findings](reports/FINDINGS.md),
[quality results](reports/quality.json) and [store ranking](reports/store_performance.csv).
Amounts are stored at six decimal places to retain the original generator's precision;
reports display two decimals. SQL and Pandas totals must agree within 0.02 currency units.

## Power BI handoff

[Exact build guide](powerbi/BUILD_GUIDE.md), [relationship specification](powerbi/semantic_model.json)
and [DAX measures](powerbi/measures.dax). The JSON is a portable specification, not a native
Power BI semantic-model file. Import the normalized CSVs, create the documented relationships
and measures, and verify all cards before publishing a PBIX. Power BI and Snowflake execution
are **NOT VERIFIED**. Do not describe this repository as an existing interactive dashboard.

## Original work and limitations

The original Python generators, lookup workbook, ER workbook, backup scripts and CSVs remain
available. Some legacy generators use machine-specific paths and unseeded random generation;
they are historical source-generation examples, not the reproducible build entry point.
The supported build consumes the preserved, hash-verified dataset. Random attributes do not
support causal commercial recommendations. Shipping treatment is inherited, not a profit definition.

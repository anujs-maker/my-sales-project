import copy
import tempfile
import unittest
from pathlib import Path
import pandas as pd
from pipeline import build, prepare_dimensions, prepare_facts, validate, verify_sources


class WarehouseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dims = prepare_dimensions()
        cls.facts = prepare_facts().head(100).copy()

    def test_source_identity(self):
        verify_sources()

    def test_stable_dimension_ids(self):
        for name, df in prepare_dimensions().items():
            pd.testing.assert_frame_equal(df, self.dims[name])

    def test_orphan_rejected(self):
        facts = self.facts.copy()
        facts.loc[0, 'ProductID'] = -1
        with self.assertRaisesRegex(ValueError, 'orphan'):
            validate(self.dims, facts)

    def test_duplicate_dimension_rejected(self):
        dims = copy.deepcopy(self.dims)
        dims['DimStore'].loc[1, 'StoreID'] = 1
        with self.assertRaisesRegex(ValueError, 'primary key'):
            validate(dims, self.facts)

    def test_amount_error_rejected(self):
        facts = self.facts.copy()
        facts.loc[0, 'TotalAmount'] += 1
        with self.assertRaisesRegex(ValueError, 'identity'):
            validate(self.dims, facts)

    def test_full_build_and_rerun(self):
        with tempfile.TemporaryDirectory() as directory:
            first = build(output=directory)
            kpis = (Path(directory) / 'kpis.csv').read_bytes()
            second = build(output=directory)
            self.assertEqual(first, second)
            self.assertEqual(first['fact_rows'], 1_000_000)
            self.assertEqual(kpis, (Path(directory) / 'kpis.csv').read_bytes())
            self.assertEqual(pd.read_csv(Path(directory) / 'kpis.csv').TotalCustomers.iloc[0], 1000)


if __name__ == '__main__':
    unittest.main()

# Executed findings — historical synthetic data

Reproduce with `python pipeline.py`. Six SQL KPIs reconcile to independent Pandas calculations.

- 1,000,000 orders across 100 store IDs, 1,000 customer IDs and 1,000 product IDs.
- Gross order amount: 549,737,436.00; AOV: 549.74; discounts: 46,706,510.27;
  shipping: 54,984,709.10. Currency is unspecified. Counts and unrounded calculations are in the outputs.
- Store 72 leads gross order amount with 5,671,008 across 10,220 records.
- Coverage is 2014-01-01 through 2024-07-27: 2024 is not a full year.
- Historical fact references pass integrity checks under the explicit source-row key convention.

These are descriptive results from randomly generated transactions, not real retail findings.
Product names/categories and transaction prices/quantities were generated independently.
Do not use these rankings to recommend actual commercial investment. TotalAmount subtracts
shipping and discounts but not product cost; it is not net profit. No measured business
improvement or original client delivery is asserted.

Validation: six unittest checks passed, including two complete builds producing identical KPIs.
Power BI rendering, DAX execution and Snowflake deployment remain NOT VERIFIED.

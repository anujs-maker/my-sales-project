# Power BI build guide — no PBIX is included

Power BI Desktop authoring/rendering has NOT BEEN VERIFIED in this repository.
The six CSV tables, relationship specification and DAX are ready for manual import.

1. Run `python pipeline.py`. Use the default historical-only build for the published checks.
2. In Power BI Desktop choose Get data → Text/CSV and import the six `build/Dim*.csv`
   and `build/FactOrders.csv` tables. Set table names to their filenames without `.csv`.
3. Set all IDs and QuantityOrdered to Whole number; Date, DateOfBirth and
   StoreOpeningDate to Date; IsWeekend to True/False; amounts to Decimal number;
   phone numbers and ZipCode to Text. Currency is unspecified: do not add INR/USD.
   Disable automatic relationships and create the five relationships in
   `semantic_model.json`, all one-to-many and single direction.
4. Mark DimDate as the date table using Date. DateID remains the relationship key.
5. Create six separate measures from `measures.dax` in FactOrders. Do not paste all six
   expressions into one measure. Format counts as integers and amounts/AOV to two decimals.
6. Add six card visuals. Add a line chart with DimDate[Date] and Total Sales;
   a bar chart with DimStore[StoreType] and Total Sales; a category bar chart
   with DimProduct[Category] and Total Sales. Add date, region and category slicers.
7. With no filters, compare every card against `reports/kpis.csv`. Expect 1,000,000
   orders and 1,000 customers. Gross sales = 549,737,436.00. Filtering StoreID 72
   must produce gross sales 5,671,008 and 10,220 orders. Remove filters afterwards.
8. Add subtitle: “Synthetic data; descriptive demonstration; currency unspecified”.
   Do not label TotalAmount as profit: it subtracts discounts and shipping, not product cost.
9. Save as `Retail_DWBI.pbix` and export screenshots of the unfiltered and StoreID 72 views.
   Only after reopening and validating the saved file should README claim a working PBIX.

## Model interpretation

Four dimensions link directly to the fact. Loyalty connects through Customer, making
this a dimensional model with a snowflaked loyalty dimension. Key assignments use frozen
source row positions; they do not reconstruct a verified historical Snowflake load.
Product/category/store rankings are illustrative because the original generator samples
attributes independently. Never infer real retail outcomes.

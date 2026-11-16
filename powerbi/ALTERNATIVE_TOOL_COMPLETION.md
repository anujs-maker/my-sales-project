# Alternative Tool Completion Guide

## Power BI alternative: self-contained HTML dashboard

File: `retail-executive-dashboard.html`

This dashboard is built from the validated Retail DWBI outputs and includes:

- Executive KPI cards: sales, orders, customers, average order value, discounts, shipping
- Top-store comparison bars
- SQL/Pandas KPI reconciliation table
- Searchable store-performance table
- Synthetic-data disclosure and Power BI limitation notice

It is suitable for recruiter review and portfolio sharing, but it is **not** a native `.pbix` file and should never be described as one.

## Snowflake alternative: local DuckDB warehouse validation

The Retail pipeline uses DuckDB as a local, zero-credential warehouse substitute. It executes the same practical warehouse checks expected in a Snowflake handoff:

- deterministic dimension keys
- primary-key and foreign-key validation
- null and duplicate checks
- amount-identity checks
- six KPI SQL/Pandas reconciliation
- rerunnable output generation

Snowflake deployment remains a separate platform validation step because no authorized Snowflake account/credentials were available. The repository includes the DDL, SQL, semantic model and build guide needed to move the validated logic into Snowflake.

## Honest completion status

The portfolio is complete for the available environment using these alternatives. Native Power BI and Snowflake execution are intentionally marked unverified rather than fabricated.

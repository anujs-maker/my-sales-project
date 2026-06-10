# End-to-End DWBI Project
## Retail Data Warehouse & Business Intelligence System

## 📌 Project Overview

This is a real-world End-to-End Data Warehouse & Business Intelligence (DWBI) project built for a retail business use case.

It demonstrates how raw transactional data is transformed into a business-ready analytics system using:

Star Schema Data Modeling
SQL-based Data Warehouse design (Snowflake-ready)
Power BI dashboards for decision-making
DAX-based KPI calculations
Business-driven reporting & insights layer

The goal is to enable data-driven decision making across sales, customers, products, stores, and loyalty programs.

🏗️ ## Data Warehouse Architecture
   ## Data Pipeline Flow
    Raw Data (CSV / Transactions)
          ↓
    Python (Data Processing / Cleaning)
          ↓
    Snowflake (Data Warehouse - Star Schema)
          ↓
    SQL (Transformations & Modeling)
          ↓
    Power BI (Dashboards & KPIs)
          ↓
    Business Insights & Decision Making


## This project follows a Star Schema Design Pattern:

                     DimDate
                        |
    DimCustomer —— FactOrders —— DimProduct
                        |
                     DimStore
                        |
             DimLoyaltyProgram (Reference Dimension)
             
🧱## Data Model Design
📅 DimDate (Time Intelligence Layer)

Supports all time-based analysis.

Attributes:

DateID (PK)
Date
DayOfWeek
Month
Quarter
Year
IsWeekend

## Business Purpose:

Sales trends
Seasonality analysis
Weekday vs weekend behavior
👤 DimCustomer (Customer Intelligence Layer)

Stores customer demographic and behavioral attributes.

## Attributes:

CustomerID (PK)
Name, Gender
DateOfBirth
Email, Address
City, State, Country
LoyaltyProgramID

## Business Purpose:

Customer segmentation
Targeted marketing
Loyalty analysis
Age-based insights
📦 DimProduct (Product Intelligence Layer)

## Attributes:

ProductID (PK)
ProductName
Category
Brand
UnitPrice

## Business Purpose:

Category performance
Product demand analysis
Pricing strategy optimization
🏬 DimStore (Operational Intelligence Layer)

## Attributes:

StoreID (PK)
StoreType
Location details
ManagerName
Opening Date

## Business Purpose:

Store benchmarking
Regional performance
Operational efficiency
🎁 DimLoyaltyProgram (Retention Layer)

## Attributes:

LoyaltyProgramID
ProgramName
Tier
Points

## Business Purpose:

Customer retention analysis
Tier-based revenue contribution
Loyalty effectiveness tracking
🧾 Fact Table – FactOrders

## Central transactional fact table.

Measures:

OrderID
DateID (FK)
CustomerID (FK)
ProductID (FK)
StoreID (FK)
QuantityOrdered
OrderAmount
DiscountAmount
ShippingCost
TotalAmount

## Business Purpose:

Revenue tracking
Sales performance analysis
Profitability insights
Operational reporting
🎯 Business Problems Solved

## This DWBI system solves real business problems:

## 📊 Sales Analytics
Revenue trends across time
Store-wise sales performance
Product category performance

## 👤 Customer Analytics
Customer segmentation (age, gender, loyalty tier)
High-value customer identification
Behavioral analysis

## 🏬 Store Analytics
Store performance comparison
Region-wise profitability
Underperforming store detection

## 📦 Product Analytics
Best-selling categories
Brand performance comparison
Pricing effectiveness
📊 Power BI Dashboard Design
🧭 Section 1: Header & Filters Layer

## Components:

Dashboard title & branding
Filters:
Region
Category
Date

## Business Value:

Dynamic filtering
Multi-dimensional analysis
User-driven exploration
📊 Section 2: KPI Layer (Executive Dashboard)
Key KPIs:
💰 Total Sales
🧾 Total Orders
👤 Total Customers
📊 Average Order Value
💸 Total Discount
🚚 Total Shipping Cost

## Business Value:

Executive summary view
Real-time performance tracking
Financial health monitoring
📈 Section 3: Performance Reporting Layer

## Visuals:

Store Type → Pie Chart
Region & Year → Line Chart
Region-wise Sales → Clustered Bar Chart

## Business Value:

Store benchmarking
Regional growth tracking
Trend analysis over time
👥 Section 4: Customer & Product Intelligence Layer

## Visuals:

Program Tier → Donut Chart
Age Group → Bar/Funnel Chart
Category → Tree Map

## Business Value:

Customer segmentation
Target marketing strategy
Product portfolio optimization

## 📊 Power BI Measures (DAX)
Total Sales = SUM(FactOrders[OrderAmount])

Total Orders = COUNT(FactOrders[OrderID])

Total Discount = SUM(FactOrders[DiscountAmount])

Total Shipping Cost = SUM(FactOrders[ShippingCost])

Average Order Value = AVERAGE(FactOrders[OrderAmount])

Total Customers = DISTINCTCOUNT(FactOrders[CustomerID])

## 👤 Calculated Columns
🎂 Age
Age =
DATEDIFF(DimCustomer[DateOfBirth], TODAY(), YEAR)

## 👥 Age Group
Age Group =
IF(DimCustomer[Age] < 18, "Minor",
IF(DimCustomer[Age] < 25, "18-24",
IF(DimCustomer[Age] < 35, "25-34",
IF(DimCustomer[Age] < 45, "35-44",
IF(DimCustomer[Age] < 55, "45-54",
IF(DimCustomer[Age] < 65, "55-64",
"65+")))))))

##  📈 Business Impact & Insights Layer (IMPORTANT)

This project enables real business decisions:

💡 Strategic Insights:
Which store type generates highest revenue
Which region is underperforming
Which category should be expanded
Which customer segment is most valuable

🎯 Marketing Impact:
Age-based targeting campaigns
Loyalty tier-based promotions
Category-based recommendations

📦 Operational Impact:
Store performance optimization
Discount strategy evaluation
Shipping cost efficiency analysis

📊 Executive Decision Support:
KPI dashboards for leadership
Revenue trend monitoring
Customer retention insights

## 🧠 Key Features
End-to-End DWBI pipeline
Star Schema Data Warehouse
Business KPI Layer
Power BI Interactive Dashboard
Customer Segmentation Model
Retail Analytics System
Insight-driven reporting layer

## 🧰 Tech Stack

SQL (Data Modeling)
Snowflake (Data Warehouse)
Python (Data Processing)
Power BI (Visualization)
DAX (Business Calculations)
Star Schema Design

## 🚀 Future Enhancements
ETL automation using dbt / Airflow
Real-time streaming pipeline
Advanced predictive analytics
Cloud deployment (AWS / Azure / Snowflake)
AI-based demand forecasting

## 🧑‍💻 Skills Demonstrated
Data Warehouse Architecture
Dimensional Modeling (Star Schema)
SQL Development
Power BI Dashboarding
Business Intelligence Design
KPI & Metrics Design
Retail Analytics Thinking
📌 Final Note

This project represents a production-style retail analytics system that converts raw data into actionable business insights using a structured DWBI approach.

👤 Author - Anuj Sharma

Domain: Data Analytics | Data Engineering | Business Intelligence
Focus: End-to-End Data Warehouse + BI Systems

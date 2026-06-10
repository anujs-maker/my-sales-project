# 📊 End-to-End DWBI Project

## Retail Data Warehouse & Business Intelligence System

## 📌 Project Overview

This is a real-world End-to-End Data Warehouse & Business Intelligence (DWBI) project built for a retail business use case.

It demonstrates how raw transactional data is transformed into a business-ready analytics system using:

* Star Schema Data Modeling
* SQL-based Data Warehouse Design (Snowflake)
* Power BI Dashboards for Decision Making
* DAX-based KPI Calculations
* Business-driven Reporting & Insights

### 🎯 Project Goal

Enable data-driven decision making across:

* Sales
* Customers
* Products
* Stores
* Loyalty Programs

---

## 🏗️ Data Warehouse Architecture

### 🔄 Data Pipeline Flow

```text
Raw Data (CSV / Transactions)
          ↓
Python (Data Processing & Cleaning)
          ↓
Snowflake (Data Warehouse - Star Schema)
          ↓
SQL (Transformations & Modeling)
          ↓
Power BI (Dashboards & KPIs)
          ↓
Business Insights & Decision Making
```

### ⭐ Star Schema Design

```text
                     DimDate
                        |
DimCustomer —— FactOrders —— DimProduct
                        |
                     DimStore
                        |
             DimLoyaltyProgram
```

---

## 🧱 Data Model Design

### 📅 DimDate (Time Intelligence Layer)

#### Attributes

* DateID (PK)
* Date
* DayOfWeek
* Month
* Quarter
* Year
* IsWeekend

#### Business Purpose

* Sales Trends
* Seasonality Analysis
* Weekday vs Weekend Analysis

---

### 👤 DimCustomer (Customer Intelligence Layer)

#### Attributes

* CustomerID (PK)
* Name
* Gender
* DateOfBirth
* Email
* Address
* City
* State
* Country
* LoyaltyProgramID

#### Business Purpose

* Customer Segmentation
* Targeted Marketing
* Loyalty Analysis
* Age-based Insights

---

### 📦 DimProduct (Product Intelligence Layer)

#### Attributes

* ProductID (PK)
* ProductName
* Category
* Brand
* UnitPrice

#### Business Purpose

* Product Performance Analysis
* Category Analysis
* Pricing Optimization

---

### 🏬 DimStore (Operational Intelligence Layer)

#### Attributes

* StoreID (PK)
* StoreType
* Location Details
* Manager Name
* Opening Date

#### Business Purpose

* Store Benchmarking
* Regional Analysis
* Operational Efficiency

---

### 🎁 DimLoyaltyProgram (Retention Layer)

#### Attributes

* LoyaltyProgramID
* ProgramName
* ProgramTier
* PointsAccrued

#### Business Purpose

* Customer Retention Analysis
* Loyalty Performance Tracking
* Tier-based Revenue Analysis

---

### 🧾 FactOrders

#### Measures

* OrderID
* DateID
* CustomerID
* ProductID
* StoreID
* QuantityOrdered
* OrderAmount
* DiscountAmount
* ShippingCost
* TotalAmount

#### Business Purpose

* Revenue Tracking
* Sales Analysis
* Profitability Reporting
* Operational Monitoring

---

## 🎯 Business Problems Solved

### 📊 Sales Analytics

* Revenue Trends Across Time
* Store-wise Sales Performance
* Product Category Analysis

### 👤 Customer Analytics

* Customer Segmentation
* High-value Customer Identification
* Behavioral Analysis

### 🏬 Store Analytics

* Store Performance Comparison
* Regional Profitability Analysis
* Underperforming Store Detection

### 📦 Product Analytics

* Best-selling Categories
* Brand Performance Comparison
* Pricing Effectiveness Analysis

---

## 📊 Power BI Dashboard Design

### 🧭 Section 1: Header & Filters Layer

#### Filters

* Region
* Category
* Date

#### Business Value

* Dynamic Filtering
* Multi-dimensional Analysis
* Self-service Reporting

---

### 📈 Section 2: Executive KPI Dashboard

#### KPIs

* 💰 Total Sales
* 🧾 Total Orders
* 👤 Total Customers
* 📊 Average Order Value
* 💸 Total Discount
* 🚚 Total Shipping Cost

#### Business Value

* Executive Monitoring
* Financial Performance Tracking
* KPI Visibility

---

### 📊 Section 3: Performance Reporting Layer

#### Visuals

* Amount by Store Type (Pie Chart)
* Amount by Region & Year (Line Chart)
* Region-wise Amount (Clustered Bar Chart)

#### Business Value

* Store Benchmarking
* Regional Growth Analysis
* Trend Monitoring

---

### 👥 Section 4: Customer & Product Intelligence Layer

#### Visuals

* Program Tier (Donut Chart)
* Age Group (Bar/Funnel Chart)
* Category (Tree Map)

#### Business Value

* Customer Segmentation
* Marketing Optimization
* Product Portfolio Analysis

---

## 📐 Power BI Measures (DAX)

```DAX
Total Sales = SUM(FactOrders[OrderAmount])

Total Orders = COUNT(FactOrders[OrderID])

Total Discount = SUM(FactOrders[DiscountAmount])

Total Shipping Cost = SUM(FactOrders[ShippingCost])

Average Order Value = AVERAGE(FactOrders[OrderAmount])

Total Customers = DISTINCTCOUNT(FactOrders[CustomerID])
```

---

## 👤 Calculated Columns

### 🎂 Age

```DAX
Age =
DATEDIFF(DimCustomer[DateOfBirth], TODAY(), YEAR)
```

### 👥 Age Group

```DAX
Age Group =
IF(DimCustomer[Age] < 18, "Minor",
IF(DimCustomer[Age] < 25, "18-24",
IF(DimCustomer[Age] < 35, "25-34",
IF(DimCustomer[Age] < 45, "35-44",
IF(DimCustomer[Age] < 55, "45-54",
IF(DimCustomer[Age] < 65, "55-64",
"65+")))))))
```

---

## 📈 Business Impact & Insights

### 💡 Strategic Insights

* Identify Top Performing Store Types
* Detect Underperforming Regions
* Expand High-Revenue Categories
* Identify High-Value Customer Segments

### 🎯 Marketing Impact

* Age-based Targeting Campaigns
* Loyalty Tier Promotions
* Category-based Recommendations

### 📦 Operational Impact

* Store Performance Optimization
* Discount Strategy Evaluation
* Shipping Cost Efficiency Analysis

### 📊 Executive Decision Support

* KPI Dashboards for Leadership
* Revenue Trend Monitoring
* Customer Retention Insights

---

## 🧠 Key Features

* End-to-End DWBI Pipeline
* Star Schema Data Warehouse
* KPI-driven Analytics
* Power BI Interactive Dashboard
* Customer Segmentation Model
* Retail Analytics Solution
* Insight-driven Reporting

---

## 🧰 Tech Stack

* SQL
* Snowflake
* Python
* Power BI
* DAX
* Star Schema Design

---

## 🧑‍💻 Skills Demonstrated

* Data Warehouse Architecture
* Dimensional Modeling
* SQL Development
* Power BI Dashboarding
* Business Intelligence Design
* KPI Development
* Retail Analytics

---

## 🚀 Future Enhancements

* dbt Integration
* Airflow Automation
* Real-time Data Pipelines
* Predictive Analytics
* Cloud Deployment
* AI-based Demand Forecasting

---

## 👤 Author

**Anuj Sharma**

**Domain:** Data Analytics | Data Engineering | Business Intelligence

**Focus:** End-to-End Data Warehouse & Analytics Solutions

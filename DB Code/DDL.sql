-- Executed locally with DuckDB. Snowflake execution NOT VERIFIED.
-- Keys supplied explicitly; no ingestion-time identity assignment.
CREATE TABLE DimDate (DateID INTEGER PRIMARY KEY, Date DATE NOT NULL, DayOfWeek INTEGER, Month INTEGER, Quarter INTEGER, Year INTEGER, IsWeekend BOOLEAN);
CREATE TABLE DimLoyaltyProgram (LoyaltyProgramID INTEGER PRIMARY KEY, ProgramName VARCHAR, ProgramTier VARCHAR, PointsAccrued INTEGER);
CREATE TABLE DimCustomer (
 CustomerID INTEGER PRIMARY KEY, FirstName VARCHAR, LastName VARCHAR, Gender VARCHAR,
 DateOfBirth DATE, Email VARCHAR, PhoneNumber VARCHAR, Address VARCHAR, City VARCHAR,
 State VARCHAR, ZipCode VARCHAR, Country VARCHAR,
 LoyaltyProgramID INTEGER REFERENCES DimLoyaltyProgram(LoyaltyProgramID));
CREATE TABLE DimProduct (ProductID INTEGER PRIMARY KEY, ProductName VARCHAR, Category VARCHAR, Brand VARCHAR, UnitPrice DECIMAL(20,6));
CREATE TABLE DimStore (
 StoreID INTEGER PRIMARY KEY, StoreName VARCHAR, StoreType VARCHAR, StoreOpeningDate DATE,
 Address VARCHAR, City VARCHAR, State VARCHAR, Country VARCHAR, Region VARCHAR, ManagerName VARCHAR);
CREATE TABLE FactOrders (
 OrderID BIGINT PRIMARY KEY, DateID INTEGER NOT NULL REFERENCES DimDate(DateID),
 CustomerID INTEGER NOT NULL REFERENCES DimCustomer(CustomerID),
 ProductID INTEGER NOT NULL REFERENCES DimProduct(ProductID),
 StoreID INTEGER NOT NULL REFERENCES DimStore(StoreID), QuantityOrdered INTEGER NOT NULL,
 OrderAmount DECIMAL(20,6) NOT NULL, DiscountAmount DECIMAL(20,6) NOT NULL,
 ShippingCost DECIMAL(20,6) NOT NULL, TotalAmount DECIMAL(20,6) NOT NULL,
 SourceFile VARCHAR NOT NULL, SourceRow BIGINT NOT NULL,
 UNIQUE(SourceFile, SourceRow), CHECK(QuantityOrdered > 0), CHECK(OrderAmount >= 0));

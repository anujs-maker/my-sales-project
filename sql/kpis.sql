-- Grain: one synthetic source row = one order. Currency is unspecified.
SELECT SUM(OrderAmount) AS TotalSales,
       COUNT(DISTINCT OrderID) AS TotalOrders,
       COUNT(DISTINCT CustomerID) AS TotalCustomers,
       SUM(OrderAmount) / NULLIF(COUNT(DISTINCT OrderID), 0) AS AverageOrderValue,
       SUM(DiscountAmount) AS TotalDiscount,
       SUM(ShippingCost) AS TotalShippingCost
FROM FactOrders;

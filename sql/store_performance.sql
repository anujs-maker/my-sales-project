-- Synthetic rankings, not evidence for real store investment decisions.
SELECT StoreID, COUNT(*) AS Orders, SUM(OrderAmount) AS GrossOrderAmount,
       DENSE_RANK() OVER (ORDER BY SUM(OrderAmount) DESC) AS SalesRank
FROM FactOrders GROUP BY StoreID ORDER BY SalesRank, StoreID;

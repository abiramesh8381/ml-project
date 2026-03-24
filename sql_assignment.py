import pandas as pd
import sqlite3

# -----------------------------
# Setup: Load datasets into SQLite
# -----------------------------
customers_url = "https://raw.githubusercontent.com/graphql-compose/graphql-compose-examples/master/examples/northwind/data/csv/customers.csv"
orders_url = "https://raw.githubusercontent.com/graphql-compose/graphql-compose-examples/master/examples/northwind/data/csv/orders.csv"

customers_df = pd.read_csv(customers_url)
orders_df = pd.read_csv(orders_url)

conn = sqlite3.connect(":memory:")
customers_df.to_sql("customers", conn, index=False, if_exists="replace")
orders_df.to_sql("orders", conn, index=False, if_exists="replace")

# -----------------------------
# Task 1 — Aggregation and Grouping
# -----------------------------
print("\n--- Task 1: Aggregation and Grouping ---")
query1 = """
SELECT 
    CustomerID,
    COUNT(OrderID) AS order_count,
    SUM(Freight) AS total_freight,
    AVG(Freight) AS avg_freight
FROM orders
GROUP BY CustomerID
ORDER BY total_freight DESC
LIMIT 10;
"""
task1_result = pd.read_sql_query(query1, conn)
print(task1_result)

# -----------------------------
# Task 2 — WHERE vs. HAVING
# -----------------------------
print("\n--- Task 2A: WHERE before aggregation ---")
queryA = """
SELECT 
    CustomerID,
    COUNT(OrderID) AS high_freight_orders
FROM orders
WHERE Freight > 50
GROUP BY CustomerID;
"""
resultA = pd.read_sql_query(queryA, conn)
print(resultA)

print("\n--- Task 2B: HAVING after aggregation ---")
queryB = """
SELECT 
    CustomerID,
    SUM(Freight) AS total_freight
FROM orders
GROUP BY CustomerID
HAVING SUM(Freight) > 500;
"""
resultB = pd.read_sql_query(queryB, conn)
print(resultB)

print("\nExplanation:")
print("WHERE filters rows before aggregation, so Query A only counts orders where Freight > 50.")
print("HAVING filters groups after aggregation, so Query B sums all orders per customer and keeps only those with total freight > 500.")

# -----------------------------
# Task 3 — JOIN and Aggregation
# -----------------------------
print("\n--- Task 3A: INNER JOIN (customers with orders only) ---")
query_inner = """
SELECT 
    c.CompanyName,
    c.Country,
    COUNT(o.OrderID) AS order_count,
    SUM(o.Freight) AS total_freight
FROM customers c
INNER JOIN orders o
    ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, c.CompanyName, c.Country;
"""
result_inner = pd.read_sql_query(query_inner, conn)
print(result_inner)

print("\n--- Task 3B: LEFT JOIN (all customers, including those with no orders) ---")
query_left = """
SELECT 
    c.CompanyName,
    c.Country,
    COUNT(o.OrderID) AS order_count,
    COALESCE(SUM(o.Freight), 0) AS total_freight
FROM customers c
LEFT JOIN orders o
    ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, c.CompanyName, c.Country;
"""
result_left = pd.read_sql_query(query_left, conn)
print(result_left)

print("\nExplanation:")
print("INNER JOIN returns only customers who have placed orders.")
print("LEFT JOIN returns all customers, including those with no orders. For them, order_count = 0 and total_freight = 0 (using COALESCE).")

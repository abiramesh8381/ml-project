import pandas as pd
import random

# -----------------------------
# Step 1: Create synthetic dataset
# -----------------------------
random.seed(42)

regions = ['North', 'South', 'East', 'West']
categories = ['Electronics', 'Clothing', 'Home & Garden', 'Sports', 'Books']
salespersons = ['Alice', 'Bob', 'Carol', 'David', 'Emma', 'Frank']

data = {
    'transaction_id': range(1001, 1201),
    'region': [random.choice(regions) for _ in range(200)],
    'category': [random.choice(categories) for _ in range(200)],
    'salesperson': [random.choice(salespersons) for _ in range(200)],
    'sales_amount': [round(random.uniform(50, 5000), 2) for _ in range(200)],
    'customer_id': [random.randint(5000, 5100) for _ in range(200)]
}

df = pd.DataFrame(data)
print(df.head(10))
print(f"\nDataset shape: {df.shape}")

# -----------------------------
# Task 1: Basic Grouping
# -----------------------------
print("\n--- Task 1: Basic Grouping ---")

# Total sales per region
regional_sales = df.groupby('region')['sales_amount'].sum().reset_index()
regional_sales = regional_sales.sort_values('sales_amount', ascending=False)
print("\nTotal sales per region:\n", regional_sales)

# Transaction count per category
category_counts = df.groupby('category')['transaction_id'].count().reset_index()
print("\nTransaction count per category:\n", category_counts)

# Average sales per salesperson
avg_sales_per_person = df.groupby('salesperson')['sales_amount'].mean().reset_index()
print("\nAverage sales per salesperson:\n", avg_sales_per_person)

# -----------------------------
# Task 2: Multi-Column Grouping
# -----------------------------
print("\n--- Task 2: Multi-Column Grouping ---")

# Region + Category sales
region_category_sales = df.groupby(['region', 'category'])['sales_amount'].sum().reset_index()
print("\nSales by region and category:\n", region_category_sales)

# Salesperson performance metrics
salesperson_summary = df.groupby('salesperson')['sales_amount'].agg(['sum', 'mean', 'count']).reset_index()
salesperson_summary = salesperson_summary.sort_values('sum', ascending=False)
print("\nSalesperson performance summary:\n", salesperson_summary)

# Top revenue category
category_sales = df.groupby('category')['sales_amount'].sum()
top_category = category_sales.idxmax()
print("\nTop revenue category:", top_category)

# -----------------------------
# Task 3: Custom Aggregation
# -----------------------------
print("\n--- Task 3: Custom Aggregation ---")

def sales_range(x):
    return x.max() - x.min()

region_analysis = df.groupby('region')['sales_amount'].agg(['sum', 'mean', 'min', 'max', sales_range]).reset_index()
print("\nRegion analysis with custom aggregation:\n", region_analysis)

# Final summary report
final_report = df.groupby('region').agg({
    'sales_amount': ['sum', 'mean'],
    'customer_id': 'count'
}).reset_index()
print("\nFinal summary report:\n", final_report)

# Flatten multi-level columns for readability
final_report.columns = ['region', 'total_sales', 'avg_sales', 'transaction_count']
print("\nFlattened summary report:\n", final_report)

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('sales_data.csv')

df.columns = df.columns.str.strip().str.title()

# Add Total Amount column
df["Total"] = df["Quantity"] * df["Price"]

# Total sales
total_sales = df["Total"].sum()
print("Total Sales:", total_sales)

# Top selling products
top_products = df.groupby("Product")["Quantity"].sum()
print("\nTop Selling Products:\n", top_products)

# Category-wise revenue
category_sales = df.groupby("Category")["Total"].sum()
print("\nCategory-wise Revenue:\n", category_sales)

# Monthly sales trend
df["Orderdate"] = pd.to_datetime(df["Orderdate"])

df["Month"] = df["Orderdate"].dt.month
monthly_sales = df.groupby("Month")["Total"].sum()

# Plot
monthly_sales.plot(kind="bar")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

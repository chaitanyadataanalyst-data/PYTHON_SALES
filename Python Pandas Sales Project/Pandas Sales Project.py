import pandas as pd

df=pd.read_csv("sales_data.csv")
print(df)

# # 1. Load and Explore the Data

# Question 1: How many rows are in the dataset?
print(df.shape[0])

# Question 2: How many columns are in the dataset?
print(df.shape[1])

# Question 3: Display the column names.
print(df.columns)

# Question 4: Display the first 5 rows.
print(df.head(5))

# Question 5: Display the last 5 rows.
print(df.tail(5))


# # 2. Select and Filter Data

# Question 6: Display Customer_Name, City, Product and Quantity.
print(df[["Customer_Name", "City", "Product", "Quantity"]])

# Question 7: Find all orders from Mumbai.
print(df[df["City"] == "Mumbai"])

# Question 8: Find all orders where Quantity > 3.
print(df[df["Quantity"] > 3])

# Question 9: Find all Electronics orders.
print(df[df["Category"] == "Electronics"])


# # 3. Create Calculated Columns

# Question 10: Calculate Total_Sales = (Quantity × Unit_Price) - Discount
df["Total_Sales"] = (df["Quantity"] * df["Unit_Price"]) - df["Discount"]
print(df["Total_Sales"])

# Question 11: Create Sales_Level: High >= 50,000; Medium >= 10,000; otherwise Low.
df["Sales_Level"] = df["Total_Sales"].apply(
    lambda x: "High" if x >= 50000 else "Medium" if x >= 10000 else "Low"
)


# # 4. Advanced Filtering

# Question 12: Find orders whose Total_Sales > 20,000.
print(df[df["Total_Sales"] > 20000])

# Question 13: Find Mumbai orders whose Total_Sales > 20,000.
print(df[(df["City"] == "Mumbai") & (df["Total_Sales"] > 20000)])

# Question 14: Find Electronics orders where Quantity >= 2.
print(df[(df["Category"] == "Electronics") & (df["Quantity"] >= 2)])


# # 5. GroupBy Analysis

# Question 15: Calculate total sales by city.
print(df.groupby("City")["Total_Sales"].sum())

# Question 16: Calculate total sales by category.
print(df.groupby("Category")["Total_Sales"].sum())

# Question 17: Calculate total quantity sold by product.
print(df.groupby("Product")["Quantity"].sum())


# # 6. Sorting and Top Performers

# Question 18: Find the top 5 highest-sales orders.
highest_sales = df.sort_values("Total_Sales", ascending=False)
print(highest_sales.head(5))

# Question 19: Sort city-wise total sales from highest to lowest.
group_city = df.groupby("City")["Total_Sales"].sum()
sort_city = group_city.sort_values(ascending=False)
print(sort_city)


# # 7. Business Questions

# Question 20: Which city generated the highest total sales?
highest_sales = df.groupby("City")["Total_Sales"].sum()
sort_city = highest_sales.sort_values(ascending=False)
print(sort_city.head(1))

# Question 21: Which product generated the highest total sales?
high_sale = df.groupby("Product")["Total_Sales"].sum()
sort_value = high_sale.sort_values(ascending=False)
print(sort_value.head(1))

# Question 22: Which category generated the highest total sales?
high_sale = df.groupby("Category")["Total_Sales"].sum()
sort_value = high_sale.sort_values(ascending=False)
print(sort_value.head(1))

# Question 23: Find the highest-value order.
highest_value_order = df.sort_values("Total_Sales", ascending=False)
print(highest_value_order.head(1))

# Question 24: Calculate the average order value.
print(df["Total_Sales"].mean())

# Question 25: Calculate total revenue.
print(df["Total_Sales"].sum())

# Question 26: How many orders were placed?
print(df["Order_ID"].count())

# Question 27: Count High, Medium and Low-value orders.
df["sales_category"] = df["Total_Sales"].apply(
    lambda x: "High" if x >= 50000 else "Medium" if x >= 10000 else "Low"
)
count = df["sales_category"].value_counts()
print(count)


# # 8. Final Sales Report Code

# Question 28: Generate the key metrics for a final sales report.
# 1. Total Orders
print(df["Order_ID"].count())

# 2. Total Revenue
print(df["Total_Sales"].sum())

# 3. Average Order Value
print(df["Total_Sales"].mean())

# 4. Best City
high_sale = df.groupby("City")["Total_Sales"].sum()
sort_city = high_sale.sort_values(ascending=False)
print(sort_city.head(1))

# 5. Best Product
high_sale = df.groupby("Product")["Total_Sales"].sum()
sort_product = high_sale.sort_values(ascending=False)
print(sort_product.head(1))

# 6. Best Category
high_sale = df.groupby("Category")["Total_Sales"].sum()
sort_category = high_sale.sort_values(ascending=False)
print(sort_category.head(1))

# 7. High-value orders
df["order_category"] = df["Total_Sales"].apply(
    lambda x: "High" if x >= 50000 else "Medium" if x >= 10000 else "Low"
)
High_value_ord = df[df["order_category"] == "High"]
print(High_value_ord)

# 8. Medium-value orders
Medium_value_ord = df[df["order_category"] == "Medium"]
print(Medium_value_ord)

# 9. Low-value orders
Low_value_ord = df[df["order_category"] == "Low"]
print(Low_value_ord)


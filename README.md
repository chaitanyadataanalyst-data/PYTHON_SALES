# 📊 Sales Data Analysis with Pandas

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green?logo=pandas)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📌 Project Overview
This project demonstrates Exploratory Data Analysis (EDA), business insights, and report generation using only Pandas on a retail sales dataset.  
The analysis answers 28 structured questions ranging from basic exploration to advanced business queries.

## 📂 Dataset
- sales_data.csv  
  Contains customer orders with fields such as:
  -  Order ID
  -  Customer Name
  -  City
  -  Product
  -  Category
  -  Quantity
  -  Unit Price
  -  Discount

## 🔎 Analysis Workflow

### 1. Load & Explore Data
- Count rows and columns  
- Display column names  
- Show first and last 5 rows  

### 2. Select & Filter Data
- Select specific columns (Customer, City, Product, Quantity)  
- Filter orders by city (e.g., Mumbai)  
- Filter by quantity and category  

### 3. Create Calculated Columns
-  Total Sales = (Quantity × Unit Price) - Discount  
-  Sales Level classification:  
- High ≥ 50,000  
- Medium ≥ 10,000  
- Low otherwise  

### 4. Advanced Filtering
- Orders with `Total Sales > 20,000`  
- Mumbai orders with `Total Sales > 20,000`  
- Electronics orders with `Quantity ≥ 2`  

### 5. GroupBy Analysis
- Total sales by city  
- Total sales by category  
- Total quantity sold by product  

### 6. Sorting & Top Performers
- Top 5 highest‑sales orders  
- City‑wise sales sorted descending  

### 7. Business Questions
- Best city, product, and category by sales  
- Highest‑value order  
- Average order value  
- Total revenue  
- Number of orders  
- Count of High, Medium, Low orders  

### 8. Final Sales Report
Key metrics generated:
- Total Orders
- Total Revenue  
- Average Order Value 
- Best City  
- Best Product  
- Best Category  
- Segmentation of High, Medium, Low orders  

## 📈 Key Insights
- Mumbai emerged as a top‑performing city.  
- Electronics category contributed significantly to revenue.  
- High‑value orders (≥ 50,000) form a smaller but crucial segment.  
- Average order value provides a benchmark for customer spending.  

## 🛠️ Tools & Libraries
- Python 
- Pandas

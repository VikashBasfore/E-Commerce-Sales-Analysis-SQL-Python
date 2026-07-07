# 🛒 E-Commerce Sales Analysis using SQL & Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?logo=mysql)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-blue?logo=pandas)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)

---

## 📌 Project Overview

This project demonstrates an end-to-end **E-Commerce Sales Analysis** using **Python**, **MySQL**, and **SQL**.

The project starts by importing multiple CSV files into a MySQL database using Python, followed by performing business analysis using SQL queries. Finally, Python is used to visualize important business insights.

The primary objective is to demonstrate practical SQL, database management, and data analysis skills through real-world business scenarios.

---

## 🎯 Business Objectives

The analysis focuses on answering key business questions, including:

- Customer distribution analysis
- Order trend analysis
- Revenue analysis
- Product category performance
- Seller performance
- Payment behavior
- Customer retention
- Year-over-Year sales growth
- Running total (Cumulative Sales)
- Business KPI reporting

---

## 🛠 Tech Stack

- Python
- MySQL
- SQL
- Pandas
- Matplotlib
- Jupyter Notebook

---

## 📂 Dataset Information

This project uses an E-Commerce dataset consisting of multiple relational tables.

### Tables Used

- Customers
- Orders
- Order Items
- Payments
- Products
- Sellers
- Geolocation

### Dataset Source

Kaggle Dataset

https://www.kaggle.com/models/narendrabariha/e-commerce-target-sales-dataset?select=sellers.csv

---

## 📁 Repository Structure

```
E-Commerce-Sales-Analysis/
│
├── README.md
├── requirements.txt
├── LICENSE
├── database_setup.py
├── business_queries.sql
├── E-Commerce.ipynb
|── Dataset_Link.txt
```

---

## ⚙ Project Workflow

```
CSV Files
      │
      ▼
Python (Pandas)
      │
      ▼
MySQL Database
      │
      ▼
SQL Business Analysis
      │
      ▼
Python Data Visualization
      │
      ▼
Business Insights
```

---

## 📥 Database Setup

The `database_setup.py` script automates the database creation process.

### Features

- Connects to MySQL
- Reads multiple CSV files
- Automatically creates database tables
- Detects SQL data types
- Cleans column names
- Handles NULL values
- Imports all records into MySQL

---

## 📊 Business Questions Solved

### Basic SQL Analysis

- List all unique customer cities
- Count total orders
- Analyze customer distribution by state
- Monthly order analysis
- Payment installment analysis

### Intermediate SQL Analysis

- Revenue by product category
- Average products purchased
- Average order value
- Seller revenue analysis
- Customer purchasing behavior

### Advanced SQL Analysis

- Customer Retention Analysis
- Running Total (Cumulative Sales)
- Moving Average
- Seller Ranking
- Top Customers
- Year-over-Year Growth Analysis

---

## 🧠 SQL Concepts Used

This project demonstrates the use of:

- SELECT
- WHERE
- GROUP BY
- HAVING
- ORDER BY
- Aggregate Functions
- INNER JOIN
- LEFT JOIN
- Multiple Table Joins
- CASE WHEN
- Subqueries
- Window Functions
- SUM() OVER()
- AVG() OVER()
- ROW_NUMBER()
- RANK()
- DENSE_RANK()
- Running Total
- Moving Average

---

## 💻 Python Concepts Used

- Database Connectivity
- File Handling
- Data Import
- Data Cleaning
- Pandas DataFrames
- Data Visualization
- MySQL Integration

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/VikashBsfore/E-Commerce-Sales-Analysis.git
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download the Dataset

Download the dataset from:

https://www.kaggle.com/models/narendrabariha/e-commerce-target-sales-dataset?select=sellers.csv

Place all CSV files inside the project dataset folder.

### 4. Configure MySQL

Create a MySQL database named:

```
ecommerce
```

Update the MySQL credentials in:

```
database_setup.py
```

### 5. Import Dataset

Run:

```bash
python database_setup.py
```

### 6. Open the Notebook

Launch Jupyter Notebook and open:

```
E-Commerce.ipynb
```

Execute all cells to reproduce the analysis.

---

## 📈 Key Insights

- Analyzed customer purchasing behavior.
- Evaluated monthly sales trends.
- Identified top-performing sellers.
- Measured revenue contribution by product category.
- Calculated cumulative sales using SQL Window Functions.
- Analyzed customer retention and yearly sales growth.
- Generated business insights using SQL and Python.

---

## 📚 Skills Demonstrated

### SQL

- Advanced SQL
- Window Functions
- Analytical Queries
- Aggregate Functions
- Joins
- Business Reporting

### Python

- Pandas
- MySQL Connector
- Data Cleaning
- Data Analysis
- Visualization

### Data Analytics

- Business Analysis
- KPI Reporting
- Trend Analysis
- Customer Analytics
- Revenue Analysis

---

## 📌 Learning Outcomes

Through this project I learned:

- Importing CSV data into MySQL using Python
- Writing advanced SQL queries
- Working with relational databases
- Performing business-oriented data analysis
- Building analytical reports
- Creating visualizations using Python

---

## 🔮 Future Enhancements

- Build an interactive Power BI dashboard
- Develop a Tableau dashboard
- Perform customer segmentation
- Implement sales forecasting
- Create an interactive Streamlit application

---

## 👨‍💻 Author

**Vikash Basfore**

Aspiring Data Analyst

- GitHub: https://github.com/VikashBasfore
- LinkedIn: www.linkedin.com/in/vikash-basfore-99a95b3bb

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

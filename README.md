# 🛒 E-Commerce Sales Analysis using SQL & Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?logo=mysql)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-blue?logo=pandas)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![Status](https://img.shields.io/badge/Project-Completed-success)

---

# 📌 Project Overview

This project demonstrates an **end-to-end E-Commerce Sales Analysis** using **Python** and **MySQL**. The objective is to transform raw transactional data into meaningful business insights by combining SQL querying with Python-based analysis and visualization.

The workflow begins with importing multiple CSV files into a MySQL database using Python, followed by solving real-world business problems using SQL and presenting insights through visualizations.

This project showcases practical skills required for **Data Analyst**, **Business Analyst**, and **SQL Developer** roles.

---

# 🎯 Business Objective

The goal of this project is to analyze an E-Commerce database and answer business questions related to:

- Customer behavior
- Sales performance
- Seller performance
- Product categories
- Payment trends
- Customer retention
- Revenue growth
- Business KPIs

The analysis demonstrates how SQL can be used to support data-driven business decisions.

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Data Import & Visualization |
| MySQL | Data Storage & Querying |
| Pandas | Data Manipulation |
| Matplotlib | Data Visualization |
| Jupyter Notebook | Analysis Environment |

---

# 📂 Dataset

The project uses a Brazilian E-Commerce dataset containing multiple relational tables.

## Tables

- Customers
- Orders
- Order Items
- Payments
- Products
- Sellers
- Geolocation

These tables are connected through primary and foreign keys to perform relational analysis.

---

# ⚙ Project Workflow

```
CSV Files
     │
     ▼
Python (Pandas)
     │
     ▼
Automatic Table Creation
     │
     ▼
MySQL Database
     │
     ▼
SQL Analysis
     │
     ▼
Business Insights
     │
     ▼
Python Visualization
```

---

# 📥 Database Creation

The project begins by creating the database automatically using Python.

The script performs the following tasks:

✔ Reads multiple CSV files

✔ Connects to MySQL

✔ Creates database tables dynamically

✔ Detects SQL data types automatically

✔ Cleans column names

✔ Handles NULL values

✔ Inserts data into MySQL

This demonstrates a complete ETL (Extract, Transform, Load) process before analysis.

---

# 📊 Business Questions Solved

## Basic SQL Analysis

- List unique customer cities
- Count total orders
- Calculate total sales
- Identify customer distribution by state
- Monthly order analysis
- Payment installment analysis

---

## Intermediate SQL Analysis

- Revenue by product category
- Average products purchased
- Average order value
- Revenue contribution by category
- Customer purchasing behavior
- Seller revenue analysis

---

## Advanced SQL Analysis

- Customer Retention Analysis
- Running Total (Cumulative Sales)
- Moving Average
- Window Functions
- Ranking Sellers
- Top Customers
- Year-over-Year Growth Analysis

---

# 🧠 SQL Concepts Demonstrated

This project covers a wide range of SQL concepts including:

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
- Common Table Expressions (CTEs)
- Window Functions
- ROW_NUMBER()
- RANK()
- DENSE_RANK()
- SUM() OVER()
- AVG() OVER()
- Running Total
- Moving Average

---

# 📈 Visualizations

The project includes Python visualizations for better business understanding.

### Current Visualizations

- Cumulative Sales Trend
- Monthly Sales Trend
- Revenue by Product Category *(Recommended)*
- Top Sellers *(Recommended)*

> Screenshots can be found inside the **images/** folder.

---

# 📊 Key Business Insights

Some important findings from the analysis include:

- Sales showed consistent growth over time.
- A few product categories contributed the majority of total revenue.
- Seller revenue is concentrated among top-performing sellers.
- Installment payments are widely used by customers.
- Customer purchasing behavior varies significantly across states.
- Running totals and moving averages provide better trend analysis than monthly sales alone.

---

# 📁 Project Structure

```
E-Commerce-Sales-Analysis/
│
├── README.md
├── requirements.txt
├── LICENSE
│
├── notebook/
│     └── E-Commerce.ipynb
│
├── sql/
│     ├── database_creation.sql
│     ├── business_queries.sql
│
├── images/
│     ├── cumulative_sales.png
│     ├── monthly_orders.png
│     ├── category_revenue.png
│     └── seller_revenue.png
│
└── dataset/
      └── Dataset Link.txt
```

---

# 🚀 How to Run the Project

### Clone Repository

```bash
git clone https://github.com/yourusername/E-Commerce-Sales-Analysis.git
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Import Dataset

1. Download the dataset.
2. Update the folder path in the notebook.
3. Execute the Python script to import CSV files into MySQL.

---

### Run SQL Queries

Open the notebook and execute each SQL query sequentially.

---

### Generate Visualizations

Run the visualization cells to generate charts and business insights.

---

# 📚 Skills Demonstrated

## SQL

- Advanced SQL
- Analytical SQL
- Window Functions
- Ranking
- Running Totals
- CTEs
- Joins
- Aggregations

---

## Python

- Pandas
- Database Connectivity
- Data Import
- Data Cleaning
- Visualization

---

## Data Analytics

- Business Analysis
- KPI Reporting
- Trend Analysis
- Customer Analytics
- Revenue Analysis

---

# 🎯 Learning Outcomes

Through this project I learned:

- Designing relational database workflows
- Importing CSV data into MySQL using Python
- Writing complex SQL queries
- Solving real business problems using SQL
- Applying analytical window functions
- Building business reports
- Creating visualizations using Python

---

# 🔮 Future Improvements

Some future enhancements include:

- Build an interactive Power BI Dashboard
- Create a Tableau Dashboard
- Sales Forecasting using Machine Learning
- Customer Segmentation
- RFM Analysis
- Interactive Streamlit Dashboard

---

# 📌 Repository Highlights

✔ End-to-End Data Analysis

✔ SQL + Python Integration

✔ MySQL Database Creation

✔ Business Problem Solving

✔ Advanced SQL Window Functions

✔ Python Visualizations

✔ Recruiter-Friendly Project Structure

---

# 🙋‍♂️ Author

**Vikash Basfore**

📧 Email: your-email@example.com

💼 LinkedIn: https://linkedin.com/in/your-profile

💻 GitHub: https://github.com/yourusername

---

⭐ If you found this project useful, consider giving it a star!

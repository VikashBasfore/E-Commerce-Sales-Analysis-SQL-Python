"""
=============================================================
Project : E-Commerce Sales Analysis using SQL & Python
Author  : Vikash Basfore

Description:
This script automates the process of importing multiple
E-Commerce CSV files into a MySQL database.

Workflow:
1. Connect to MySQL database.
2. Read CSV files using Pandas.
3. Automatically detect SQL data types.
4. Create tables dynamically.
5. Handle missing values (NaN → NULL).
6. Insert records into MySQL.
7. Commit changes and close the connection.

Dataset Tables:
- Customers
- Orders
- Sellers
- Products
- Geolocation
- Payments
- Order Items

=============================================================
"""

# ============================
# Import Required Libraries
# ============================

import pandas as pd
import mysql.connector
import os

# ==========================================================
# List of CSV files and their corresponding MySQL table names
# ==========================================================

csv_files = [
    ('customers.csv', 'customers'),
    ('orders.csv', 'orders'),
    ('sellers.csv', 'sellers'),
    ('products.csv', 'products'),
    ('geolocation.csv', 'geolocation'),
    ('payments.csv', 'payments'),
    ('order_items.csv', 'order_items')
]

# ============================
# Connect to MySQL Database
# ============================

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='ecommerce'
)

cursor = conn.cursor()

# ========================================
# Folder containing all E-Commerce CSV files
# ========================================

folder_path = "C:/Users/vikas/OneDrive/Documents/PROJECTS/E-Commerce"

# =====================================================
# Function to automatically detect SQL data types
# based on Pandas DataFrame column data types
# =====================================================

def get_sql_type(dtype):
    if pd.api.types.is_integer_dtype(dtype):
        return 'INT'
    elif pd.api.types.is_float_dtype(dtype):
        return 'FLOAT'
    elif pd.api.types.is_bool_dtype(dtype):
        return 'BOOLEAN'
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return 'DATETIME'
    else:
        return 'TEXT'

# ======================================================
# Loop through every CSV file and import it into MySQL
# ======================================================

for csv_file, table_name in csv_files:

    # Create the full path of the CSV file
    file_path = os.path.join(folder_path, csv_file)

    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(file_path)

    # Replace missing values (NaN) with None
    # so MySQL stores them as NULL
    df = df.where(pd.notnull(df), None)

    # Display the number of missing values
    # for each column before insertion
    print(f"Processing {csv_file}")
    print(f"NaN values before replacement:\n{df.isnull().sum()}\n")

    # Clean column names by replacing
    # spaces, hyphens, and dots with underscores
    df.columns = [
        col.replace(' ', '_')
           .replace('-', '_')
           .replace('.', '_')
        for col in df.columns
    ]

    # ==================================================
    # Generate CREATE TABLE query dynamically
    # based on detected column data types
    # ==================================================

    columns = ', '.join([
        f'`{col}` {get_sql_type(df[col].dtype)}'
        for col in df.columns
    ])

    create_table_query = f'''
    CREATE TABLE IF NOT EXISTS `{table_name}`
    ({columns})
    '''

    cursor.execute(create_table_query)

    # ==================================================
    # Insert DataFrame rows into the MySQL table
    # ==================================================

    for _, row in df.iterrows():

        # Convert missing values to SQL NULL
        values = tuple(None if pd.isna(x) else x for x in row)

        sql = f'''
        INSERT INTO `{table_name}`
        ({', '.join(['`' + col + '`' for col in df.columns])})
        VALUES ({', '.join(['%s'] * len(row))})
        '''

        cursor.execute(sql, values)

    # Save changes for the current table
    conn.commit()

    print(f"{table_name} imported successfully.\n")

# ============================
# Close Database Connection
# ============================

conn.close()

print("===================================")
print("Database Setup Completed Successfully")
print("All CSV files imported into MySQL.")
print("===================================")

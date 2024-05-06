import sqlite3
import pandas as pd

# Connect to the database
connection = sqlite3.connect("Dental.db")
cursor = connection.cursor()

# Define the Excel file path
excel_file = r'C:\Users\sandeepkumar.singh\Gen AI Project\Sample Data.xlsx'

# Read each sheet into a separate DataFrame
dataframes = pd.read_excel(excel_file, sheet_name=None)

# Iterate through the DataFrames and create tables
for sheet_name, df in dataframes.items():
    table_name = sheet_name  # Use sheet name as table name

    # Create table based on DataFrame structure
    columns = ",".join([f"{col} {df[col].dtype.name}" for col in df.columns])
    create_table_query = f"""CREATE TABLE IF NOT EXISTS {table_name} ({columns});"""
    cursor.execute(create_table_query)

    # Insert data from DataFrame
    df.to_sql(table_name, connection, if_exists="append", index=False)

# Commit changes and close connection
connection.commit()
connection.close()

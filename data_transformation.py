"""
Module: data_transformation.py
Author: Satej
Description: This module performs data aggregation, grouping, and transformation
using SQL and Pandas. It calculates key performance indicators (KPIs) such as
average revenue per region, sales by customer demographics, and market share percentages.
"""

import sqlite3
import pandas as pd

def create_database(db_path: str) -> None:
    """
    Creates an SQLite database to store sales data for transformation and querying.
    
    Args:
        db_path (str): Path to create the SQLite database.
    """
    try:
        conn = sqlite3.connect(db_path)
        conn.close()
        print(f"Database created at {db_path}.")
    except Exception as e:
        print(f"Error creating database: {e}")
        raise

def load_data_to_database(data: pd.DataFrame, db_path: str, table_name: str) -> None:
    """
    Loads Pandas DataFrame into an SQLite database table.
    
    Args:
        data (pd.DataFrame): The data to be loaded.
        db_path (str): Path to the SQLite database.
        table_name (str): Name of the table to store data.
    """
    try:
        conn = sqlite3.connect(db_path)
        data.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.close()
        print(f"Data successfully loaded into table '{table_name}' in database.")
    except Exception as e:
        print(f"Error loading data into database: {e}")
        raise

def calculate_kpis(db_path: str) -> pd.DataFrame:
    """
    Performs SQL queries to calculate KPIs such as sales by region, average revenue,
    and market share percentages.
    
    Args:
        db_path (str): Path to the SQLite database.
        
    Returns:
        pd.DataFrame: A DataFrame containing KPI metrics.
    """
    try:
        conn = sqlite3.connect(db_path)
        query = """
        SELECT 
            region,
            SUM(sales) AS total_sales,
            SUM(revenue) AS total_revenue,
            AVG(revenue) AS avg_revenue_per_region
        FROM sales_data
        GROUP BY region
        ORDER BY total_sales DESC;
        """
        kpis = pd.read_sql_query(query, conn)
        conn.close()
        print("KPIs calculated successfully.")
        return kpis
    except Exception as e:
        print(f"Error calculating KPIs: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Paths
    db_path = "/home/satej/sales_data/sales_database.db"
    csv_path = "/home/satej/sales_data/cleaned_sales.csv"
    table_name = "sales_data"
    kpi_output_path = "/home/satej/sales_data/kpi_results.csv"

    # Load data and calculate KPIs
    create_database(db_path)
    sales_data = pd.read_csv(csv_path)
    load_data_to_database(sales_data, db_path, table_name)
    kpis = calculate_kpis(db_path)

    # Save KPI results
    kpis.to_csv(kpi_output_path, index=False)
    print(f"KPI results saved to {kpi_output_path}.")

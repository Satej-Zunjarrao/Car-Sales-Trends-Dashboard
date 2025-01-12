"""
Module: config.py
Author: Satej
Description: This configuration file stores paths and constants for the car sales trends
project, ensuring consistency and reusability across modules.
"""

# File paths
RAW_DATA_PATH = "/home/satej/sales_data/raw_sales.csv"
CLEANED_DATA_PATH = "/home/satej/sales_data/cleaned_sales.csv"
DATABASE_PATH = "/home/satej/sales_data/sales_database.db"
KPI_OUTPUT_PATH = "/home/satej/sales_data/kpi_results.csv"
TABLEAU_DATASETS_FOLDER = "/home/satej/sales_data/tableau_datasets"

# Tableau dataset exports
SALES_BY_REGION_PATH = f"{TABLEAU_DATASETS_FOLDER}/sales_by_region.csv"
SALES_BY_MODEL_PATH = f"{TABLEAU_DATASETS_FOLDER}/sales_by_model.csv"
MONTHLY_SALES_TRENDS_PATH = f"{TABLEAU_DATASETS_FOLDER}/monthly_sales_trends.csv"

# Database table name
TABLE_NAME = "sales_data"

# Visualization output paths
VISUALIZATIONS_FOLDER = "/home/satej/sales_data/visualizations"
REGION_CHART_PATH = f"{VISUALIZATIONS_FOLDER}/sales_by_region.png"
TRENDS_CHART_PATH = f"{VISUALIZATIONS_FOLDER}/sales_trends.png"
MODEL_CHART_PATH = f"{VISUALIZATIONS_FOLDER}/sales_by_model.png"

# Constants for data cleaning
CRITICAL_COLUMNS = ['Region', 'Model', 'Sales', 'Revenue', 'Date']
NUMERIC_COLUMNS = ['sales', 'revenue']

# Logging configurations (if required in future development)
LOGGING_ENABLED = True
LOG_FILE_PATH = "/home/satej/sales_data/logs/project_logs.log"

# Example usage
if __name__ == "__main__":
    print("Configuration file for Car Sales Trends Dashboard.")
    print(f"Cleaned Data Path: {CLEANED_DATA_PATH}")
    print(f"Database Path: {DATABASE_PATH}")
    print(f"Visualization Folder: {VISUALIZATIONS_FOLDER}")

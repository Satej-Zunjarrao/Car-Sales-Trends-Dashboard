"""
Module: export_to_tableau.py
Author: Satej
Description: This module exports cleaned and transformed data into formats compatible with Tableau
for interactive visualization. The focus is on generating aggregated CSV files.
"""

import pandas as pd

def export_aggregated_data(data: pd.DataFrame, output_path: str) -> None:
    """
    Exports aggregated data to a CSV file for Tableau visualization.
    
    Args:
        data (pd.DataFrame): Aggregated or transformed data.
        output_path (str): Path to save the exported CSV file.
    """
    try:
        data.to_csv(output_path, index=False)
        print(f"Aggregated data exported to {output_path}.")
    except Exception as e:
        print(f"Error exporting data: {e}")
        raise

def prepare_tableau_datasets(cleaned_data_path: str, output_folder: str) -> None:
    """
    Prepares datasets for Tableau by creating specific aggregated views, such as sales by region
    and sales by model, and saving them as CSV files.
    
    Args:
        cleaned_data_path (str): Path to the cleaned data CSV file.
        output_folder (str): Folder path to save Tableau datasets.
    """
    try:
        # Load cleaned data
        data = pd.read_csv(cleaned_data_path)

        # Aggregated dataset: Sales by region
        sales_by_region = data.groupby('region').agg({'sales': 'sum', 'revenue': 'sum'}).reset_index()
        region_output_path = f"{output_folder}/sales_by_region.csv"
        export_aggregated_data(sales_by_region, region_output_path)

        # Aggregated dataset: Sales by model
        sales_by_model = data.groupby('model').agg({'sales': 'sum', 'revenue': 'sum'}).reset_index()
        model_output_path = f"{output_folder}/sales_by_model.csv"
        export_aggregated_data(sales_by_model, model_output_path)

        # Aggregated dataset: Monthly sales trends
        data['month_year'] = pd.to_datetime(data['date']).dt.to_period('M')
        monthly_sales = data.groupby('month_year').agg({'sales': 'sum'}).reset_index()
        monthly_sales['month_year'] = monthly_sales['month_year'].astype(str)
        trends_output_path = f"{output_folder}/monthly_sales_trends.csv"
        export_aggregated_data(monthly_sales, trends_output_path)

        print("All datasets for Tableau have been prepared successfully.")
    except Exception as e:
        print(f"Error preparing Tableau datasets: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Paths
    cleaned_data_path = "/home/satej/sales_data/cleaned_sales.csv"
    output_folder = "/home/satej/sales_data/tableau_datasets"

    # Prepare Tableau datasets
    prepare_tableau_datasets(cleaned_data_path, output_folder)

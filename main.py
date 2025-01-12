"""
Module: main.py
Author: Satej
Description: Entry point for the Car Sales Trends Dashboard project. This script orchestrates the 
workflow, including data collection, cleaning, transformation, EDA, and exporting datasets for dashboard design.
"""

from data_collection_cleaning import load_csv_data, clean_data, save_cleaned_data
from data_transformation import create_database, load_data_to_database, calculate_kpis
from eda_visualizations import plot_sales_by_region, plot_sales_trends, plot_sales_by_model
from export_to_tableau import prepare_tableau_datasets
from config import (
    RAW_DATA_PATH, CLEANED_DATA_PATH, DATABASE_PATH, TABLE_NAME, KPI_OUTPUT_PATH,
    REGION_CHART_PATH, TRENDS_CHART_PATH, MODEL_CHART_PATH, TABLEAU_DATASETS_FOLDER
)


def main():
    """
    Main function that orchestrates the workflow of the Car Sales Trends Dashboard project.
    """
    print("Starting the Car Sales Trends Dashboard workflow...")

    # Step 1: Load raw data
    print("\nStep 1: Loading raw data...")
    raw_data = load_csv_data(RAW_DATA_PATH)

    # Step 2: Clean the data
    print("\nStep 2: Cleaning data...")
    cleaned_data = clean_data(raw_data)
    save_cleaned_data(cleaned_data, CLEANED_DATA_PATH)

    # Step 3: Create and load data into the database
    print("\nStep 3: Creating database and loading data...")
    create_database(DATABASE_PATH)
    load_data_to_database(cleaned_data, DATABASE_PATH, TABLE_NAME)

    # Step 4: Calculate KPIs
    print("\nStep 4: Calculating KPIs...")
    kpis = calculate_kpis(DATABASE_PATH)
    kpis.to_csv(KPI_OUTPUT_PATH, index=False)
    print(f"KPIs saved to {KPI_OUTPUT_PATH}.")

    # Step 5: Generate visualizations
    print("\nStep 5: Generating visualizations...")
    plot_sales_by_region(cleaned_data, REGION_CHART_PATH)
    plot_sales_trends(cleaned_data, TRENDS_CHART_PATH)
    plot_sales_by_model(cleaned_data, MODEL_CHART_PATH)

    # Step 6: Export datasets for Tableau
    print("\nStep 6: Preparing Tableau datasets...")
    prepare_tableau_datasets(CLEANED_DATA_PATH, TABLEAU_DATASETS_FOLDER)

    print("\nWorkflow completed successfully. All outputs are saved to their respective locations.")


if __name__ == "__main__":
    main()

"""
Module: data_collection_cleaning.py
Author: Satej
Description: This module is responsible for importing sales data from multiple sources,
cleaning and standardizing it to ensure consistency and accuracy. 
"""

import pandas as pd
import os

def load_csv_data(file_path: str) -> pd.DataFrame:
    """
    Loads data from a CSV file into a Pandas DataFrame.
    
    Args:
        file_path (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: Loaded data as a Pandas DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data successfully loaded from {file_path}.")
        return data
    except FileNotFoundError as e:
        print(f"Error: {e}. Please ensure the file path is correct.")
        raise

def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and standardizes the data by handling missing values, renaming columns,
    and ensuring proper data types.
    
    Args:
        data (pd.DataFrame): The raw data as a Pandas DataFrame.
        
    Returns:
        pd.DataFrame: Cleaned data.
    """
    print("Starting data cleaning process...")
    
    # Drop rows with missing values in critical columns
    critical_columns = ['Region', 'Model', 'Sales', 'Revenue', 'Date']
    data = data.dropna(subset=critical_columns)
    
    # Standardize column names to lowercase
    data.columns = [col.lower() for col in data.columns]
    
    # Convert 'date' column to datetime format
    if 'date' in data.columns:
        data['date'] = pd.to_datetime(data['date'])
    
    # Ensure numeric columns are properly formatted
    numeric_columns = ['sales', 'revenue']
    for col in numeric_columns:
        data[col] = pd.to_numeric(data[col], errors='coerce')
    
    print("Data cleaning completed successfully.")
    return data

def save_cleaned_data(data: pd.DataFrame, output_path: str) -> None:
    """
    Saves the cleaned data to a specified output path as a CSV file.
    
    Args:
        data (pd.DataFrame): The cleaned data.
        output_path (str): Path to save the cleaned data.
    """
    try:
        data.to_csv(output_path, index=False)
        print(f"Cleaned data saved to {output_path}.")
    except Exception as e:
        print(f"Error: {e}. Unable to save cleaned data.")
        raise

# Example usage
if __name__ == "__main__":
    # Define file paths
    input_path = "/home/satej/sales_data/raw_sales.csv"
    output_path = "/home/satej/sales_data/cleaned_sales.csv"

    # Data loading, cleaning, and saving
    raw_data = load_csv_data(input_path)
    cleaned_data = clean_data(raw_data)
    save_cleaned_data(cleaned_data, output_path)

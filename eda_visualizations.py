"""
Module: eda_visualizations.py
Author: Satej
Description: This module performs Exploratory Data Analysis (EDA) and creates visualizations 
to uncover patterns, trends, and key metrics in car sales data.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_sales_by_region(data: pd.DataFrame, output_path: str) -> None:
    """
    Creates a bar chart to visualize total sales by region.
    
    Args:
        data (pd.DataFrame): The cleaned sales data.
        output_path (str): Path to save the visualization as an image.
    """
    print("Creating bar chart for sales by region...")
    sales_by_region = data.groupby('region')['sales'].sum().sort_values(ascending=False)
    
    plt.figure(figsize=(10, 6))
    sales_by_region.plot(kind='bar', color='skyblue')
    plt.title("Total Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)
    print(f"Bar chart saved to {output_path}.")

def plot_sales_trends(data: pd.DataFrame, output_path: str) -> None:
    """
    Creates a line chart to visualize sales trends over time.
    
    Args:
        data (pd.DataFrame): The cleaned sales data.
        output_path (str): Path to save the visualization as an image.
    """
    print("Creating line chart for sales trends...")
    data['month_year'] = data['date'].dt.to_period('M')
    sales_trends = data.groupby('month_year')['sales'].sum()
    
    plt.figure(figsize=(12, 6))
    sales_trends.plot(kind='line', marker='o', color='blue')
    plt.title("Sales Trends Over Time")
    plt.xlabel("Month-Year")
    plt.ylabel("Total Sales")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path)
    print(f"Line chart saved to {output_path}.")

def plot_sales_by_model(data: pd.DataFrame, output_path: str) -> None:
    """
    Creates a pie chart to visualize sales distribution by car model.
    
    Args:
        data (pd.DataFrame): The cleaned sales data.
        output_path (str): Path to save the visualization as an image.
    """
    print("Creating pie chart for sales by car model...")
    sales_by_model = data.groupby('model')['sales'].sum().sort_values(ascending=False)
    
    plt.figure(figsize=(8, 8))
    sales_by_model.plot(kind='pie', autopct='%1.1f%%', startangle=140)
    plt.title("Sales Distribution by Car Model")
    plt.ylabel("")  # Remove the default ylabel
    plt.tight_layout()
    plt.savefig(output_path)
    print(f"Pie chart saved to {output_path}.")

# Example usage
if __name__ == "__main__":
    # Define file paths
    cleaned_data_path = "/home/satej/sales_data/cleaned_sales.csv"
    region_output_path = "/home/satej/sales_data/visualizations/sales_by_region.png"
    trends_output_path = "/home/satej/sales_data/visualizations/sales_trends.png"
    model_output_path = "/home/satej/sales_data/visualizations/sales_by_model.png"

    # Load cleaned data
    data = pd.read_csv(cleaned_data_path)

    # Generate visualizations
    plot_sales_by_region(data, region_output_path)
    plot_sales_trends(data, trends_output_path)
    plot_sales_by_model(data, model_output_path)

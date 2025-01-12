# Car-Sales-Trends-Dashboard
Designed and developed an interactive dashboard to visualize car sales trends, providing actionable insights into sales performance.

# Car Sales Trends Dashboard

## Overview
The **Car Sales Trends Dashboard** is a Python-based solution designed to analyze car sales data and visualize trends across regions, car models, and customer demographics. The project leverages data cleaning, transformation, visualization, and dashboard design techniques to create a user-friendly tool for stakeholders to make strategic decisions based on real-time and historical data.

This project includes a modular and scalable pipeline for data collection, cleaning, exploratory analysis, KPI computation, visualization, and Tableau dashboard integration.

---

## Key Features
- **Data Collection**: Imports sales data from SQL databases and CSV files.
- **Data Cleaning**: Standardizes and preprocesses data to ensure consistency.
- **Exploratory Data Analysis (EDA)**: Visualizes sales patterns, seasonal trends, and top-performing models.
- **KPI Computation**: Calculates metrics like sales growth rates, market share, and average revenue per region.
- **Visualization**: Generates insightful plots (bar, line, pie charts) to identify trends and patterns.
- **Dashboard Design**: Integrates data with Tableau to build an interactive dashboard for stakeholders.

---

## Directory Structure

plaintext
project/
│
├── data_collection_cleaning.py   # Imports and cleans raw sales data
├── eda_visualizations.py         # Generates visualizations and insights
├── data_transformation.py        # Performs data aggregation and KPI calculation
├── export_to_tableau.py          # Prepares datasets for Tableau
├── dashboard_design_notes.md     # Documentation of dashboard design elements
├── config.py                     # Stores reusable configurations and constants
├── main.py                       # Orchestrates the entire project workflow
├── README.md                     # Project documentation

---

# Modules

## 1. data_collection_cleaning.py
- Loads raw data from SQL and CSV files.
- Cleans and standardizes data for analysis.

## 2. eda_visualizations.py
- Creates visualizations such as bar, line, and pie charts.
- Highlights sales trends, regional performance, and market share.

## 3. data_transformation.py
- Uses SQL queries for data aggregation and grouping.
- Calculates KPIs like total sales, average revenue, and market share.

## 4. export_to_tableau.py
- Prepares datasets in Tableau-compatible formats.
- Generates CSV files for regional sales, model-wise performance, and monthly trends.

## 5. dashboard_design_notes.md
- Documents the design and functionality of the Tableau dashboard.
- Explains components like bar charts, pie charts, and dynamic filters.

## 6. config.py
- Centralized configuration file for paths, constants, and database details.

## 7. main.py
- Orchestrates the entire project workflow.
- Executes data collection, cleaning, transformation, visualization, and Tableau export.

---

# Contact

For queries or collaboration, feel free to reach out:

- **Name**: Satej Zunjarrao  
- **Email**: zsatej1028@gmail.com

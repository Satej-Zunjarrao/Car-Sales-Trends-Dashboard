# Dashboard Design Notes

## Author
Satej

## Overview
This document provides detailed notes on the design and structure of the interactive dashboard for visualizing car sales trends. The dashboard was built using **Tableau**, incorporating various visualization types to provide actionable insights for stakeholders.

---

## Dashboard Components

### 1. **Bar Charts: Sales by Region**
   - **Purpose**: Highlights total sales across different regions.
   - **Design Features**:
     - Bars are sorted in descending order of sales.
     - Color-coded by region for better differentiation.
   - **Interactivity**:
     - Dynamic filters to select specific time periods or car types.

### 2. **Pie Chart: Market Share by Car Model**
   - **Purpose**: Visualizes the distribution of sales by car model.
   - **Design Features**:
     - Displays market share percentages.
     - Includes a legend for easy identification of car models.
   - **Interactivity**:
     - Hover functionality shows detailed values for each segment.

### 3. **Line Chart: Monthly and Seasonal Sales Trends**
   - **Purpose**: Tracks sales performance over time, identifying seasonal patterns.
   - **Design Features**:
     - Data points marked for peak and low sales periods.
     - Smoothened lines to enhance visual clarity.
   - **Interactivity**:
     - Dropdowns to filter trends by region or car model.

### 4. **KPIs: Quick Summary of Metrics**
   - **Purpose**: Displays key performance indicators (KPIs) at the top of the dashboard.
   - **KPIs Included**:
     - Total Sales
     - Average Revenue per Region
     - Top-Performing Car Model
   - **Design Features**:
     - Bold and highlighted metrics for immediate focus.

---

## Filters and Controls
- **Dynamic Filters**:
  - Time Period: Yearly, Monthly, Weekly
  - Car Type: SUV, Sedan, Hatchback
  - Region: North, South, East, West
- **Purpose**:
  - Enable users to customize views based on their specific needs.
  - Help stakeholders drill down into specific details for analysis.

---

## Dataset Integration
- **Data Sources**:
  - Cleaned sales data from `cleaned_sales.csv`.
  - Aggregated datasets:
    - `sales_by_region.csv`
    - `sales_by_model.csv`
    - `monthly_sales_trends.csv`
- **Connection**:
  - Imported datasets into Tableau directly via the `Tableau Data Source` interface.

---

## Deployment and Sharing
- **Deployment**:
  - Published the dashboard to Tableau Public for accessibility.
  - Configured for real-time data updates by linking to a live database.
- **Sharing**:
  - Shared with stakeholders via a secure link and embedded in internal reports.

---

## Future Enhancements
- Include customer demographic visualizations.
- Add machine learning-based sales forecasting for predictive analytics.
- Automate data updates for seamless integration with real-time sources.

---

### Notes
This document serves as a guideline for replicating and enhancing the dashboard. If you have questions, contact **Satej** for additional details or clarifications.

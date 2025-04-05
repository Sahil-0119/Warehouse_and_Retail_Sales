# 📦📊 Warehouse and Retail Sales Data Analysis

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?logo=matplotlib)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Graphs-cyan?logo=seaborn)

---

## 🎯 Project Goals

This project aims to:
- Understand and explore retail and warehouse sales data across various item types and time periods.
- Perform data cleaning and summarization to gain insights.
- Visualize key trends using scatter plots, line graphs, boxplots, pie charts, and more.
- Detect outliers and patterns in sales and transfers.
- Provide a clear, visual dashboard-like analysis for decision-making or reporting.

---

## 📁 Dataset Overview

- **Filename:** `Warehouse_and_Retail_Sales.csv`
- **Columns:**
  - `ITEM TYPE`
  - `RETAIL SALES`
  - `WAREHOUSE SALES`
  - `RETAIL TRANSFERS`
  - `YEAR`
  - `MONTH`

---

## 📊 Features & Visualizations

### 📌 1. Data Summary
- View dataset information, data types, and missing values.
- Summary statistics using `describe()`.

### 🥧 2. Pie Chart: Item Type Distribution
- Visualizes the percentage of each item type in the dataset.

### 🔁 3. Scatter Plot: Retail vs Warehouse Sales
- Highlights the relationship between retail and warehouse sales across different years.

### 📈 4. Line Plot: Retail Sales by Item Type
- Multi-line graph comparing sales across item types and years.

### 🔗 5. Pairplot: Correlation Overview
- Visual relationship matrix using `pairplot()` with KDE on the diagonal.

### 🔄 6. Line Plot: Retail Transfers Over Time
- Shows retail transfers over time for each item type.

### 📦 7. Boxplot: Warehouse Sales
- Outlier detection using IQR and boxplot visualization.

### 📉 8. Stacked Area Chart: Sales Over Time
- Cumulative visual of warehouse and retail sales over time.

---

## 🛠️ Technologies Used

- [Python 3.9+](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [NumPy](https://numpy.org/)

---

## 🚀 How to Run

1. **Install dependencies**
   ```bash
   pip install pandas matplotlib seaborn numpy

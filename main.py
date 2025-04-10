import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
fd = "C:\\Users\\moon\\OneDrive\\Desktop\\Warehouse_and_Retail_Sales.csv"
data = pd.read_csv(fd)
# Display dataset information
data.info()
print("\nDataset Summary:\n", data.describe())
print("\nMissing Values in Each Column:\n", data.isnull().sum())
print("\nColumn Names:\n", data.columns)
# Counting no. of item types and their values in the dataset
item_type= data['ITEM TYPE'].value_counts() # value_counts() is used to count unique value in the column

# Creating pie chart 
plt.figure(figsize=(100, 120))  # Create a figure with the specified size
c= ['sandybrown', 'royalblue', 'navy', 'crimson', 'thistle', 'purple', 'pink']
plt.pie(item_type, labels=item_type.index, colors=c,startangle=140,autopct='%0.2f%%')#autopct is used to calculate percentage
plt.title('Distribution of Item Types with Percentage')
plt.show()


#------------------------------------------------------------------------------------------------------------------------------
#  1 creating a Scattor plot Retail V/S Warehouse Sales
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_path = "C:\\Users\\moon\\OneDrive\\Desktop\\Warehouse_and_Retail_Sales.csv" 
data = pd.read_csv(file_path)
plt.figure(figsize=(120, 100))
# Scatter plot for the data
sns.scatterplot(x='RETAIL SALES', y='WAREHOUSE SALES', hue='YEAR', data=data, palette='viridis', alpha=0.7)
plt.title('Scatter Plot: Retail Sales vs. Warehouse Sales', fontsize=18)
plt.xlabel('Retail Sales', fontsize=14)
plt.ylabel('Warehouse Sales', fontsize=14)
plt.grid(True)
plt.legend(title='Year')
plt.show()


#--------------------------------------------------------------------------------------------------------------------------------
# 2 Creating Line graph which compare sales trends over time.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
fd = "C:\\Users\\moon\\OneDrive\\Desktop\\Warehouse_and_Retail_Sales.csv"
df = pd.read_csv(fd)
# Line plot for Retail Sales per Item Type
plt.figure(figsize=(100, 60))
sns.lineplot(x="ITEM TYPE", y="RETAIL SALES", hue="YEAR", style="YEAR", markers=True, data=df, palette="coolwarm")

plt.xlabel("Item Type")
plt.ylabel("Retail Sales")
plt.title("Retail Sales by Item Type and Warehouse")
plt.xticks(rotation=45)
plt.legend(title="Warehouse")
plt.grid(True)
plt.show()

#-------------------------------------------------------------------------------------------------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
fd = "C:\\Users\\moon\\OneDrive\\Desktop\\Warehouse_and_Retail_Sales.csv"
df = pd.read_csv(fd)

# Create Pairplot (Only for Numerical Columns)
sns.pairplot(df, hue="YEAR", palette="warmcool", diag_kind="kde")

plt.show()



#-------------------------------------------------------------------------------------------------------
# 3 Stock Movement and Retail Transfers Over Time by Item Type
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_path = "C:\\Users\\moon\\OneDrive\\Desktop\\Warehouse_and_Retail_Sales.csv"
df = pd.read_csv(file_path)

# Convert YEAR and MONTH into a datetime format
df['DATE'] = pd.to_datetime(df[['YEAR', 'MONTH']].assign(DAY=1))

# Aggregate total retail transfers by date and item type
stock_movement = df.groupby(['DATE', 'ITEM TYPE'])['RETAIL TRANSFERS'].sum().reset_index()
sns.set_style("darkgrid")
plt.figure(figsize=(14, 7))
sns.lineplot(x='DATE', y='RETAIL TRANSFERS', hue='ITEM TYPE', data=stock_movement,
             marker='o', linestyle='-', linewidth=2, markersize=6, palette='tab10')
plt.xlabel('Time', fontsize=13)
plt.ylabel('Total Retail Transfers', fontsize=13)
plt.title('Stock Movement and Retail Transfers Over Time by Item Type', fontsize=16, fontweight='bold')
plt.xticks(rotation=45, fontsize=11)
plt.yticks(fontsize=11)
plt.legend(title='Item Type', fontsize=11)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

#------------------------------------------------------------------------------------------------------------------------
#   "Boxplot of Warehouse Sales"


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_path = "C:\\Users\\moon\\OneDrive\\Desktop\\Warehouse_and_Retail_Sales.csv"
df = pd.read_csv(file_path)
column = 'WAREHOUSE SALES'# we can also create for RETAIL SALES,RETAIL TRANSFERS,WAREHOUSE SALES

# Calculate Q1 (25th percentile) and Q3 (75th percentile)
Q1 = df[column].quantile(0.25)
Q3 = df[column].quantile(0.75)

# Calculate IQR (Interquartile Range)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
print("Outliers detected:")
print(outliers)
plt.figure(figsize=(8, 5))
sns.boxplot(x=df[column], color='skyblue')

# Customize plot
plt.title(f'Boxplot of {column}', fontsize=14, fontweight='bold')#Uses an f-string to dynamically insert the column name into the title.
plt.xlabel(column, fontsize=12)
plt.show()

#----------------------------------------------------------------------------------------------------------------
#  4 Stacked Area Chart: Retail and Warehouse Sales Over Time

import pandas as pd
import matplotlib.pyplot as plt
file_path = "C:\\Users\\moon\\OneDrive\\Desktop\\Warehouse_and_Retail_Sales.csv"
df = pd.read_csv(file_path)
df['DATE'] = pd.to_datetime(df[['YEAR', 'MONTH']].assign(DAY=1))#converting month and year in a single date starting with 1

# Aggregate Retail and Warehouse Sales over time
area_data = df.groupby('DATE')[['RETAIL SALES', 'WAREHOUSE SALES']].sum().reset_index()

# Plot stacked area chart
plt.figure(figsize=(14, 7))
plt.stackplot(area_data['DATE'], 
              area_data['RETAIL SALES'], 
              area_data['WAREHOUSE SALES'], 
              labels=['Retail Sales', 'Warehouse Sales'], 
              colors=['skyblue', 'lightgreen'], alpha=0.8)

plt.title('Stacked Area Chart: Retail and Warehouse Sales Over Time', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=13)
plt.ylabel('Sales', fontsize=13)
plt.legend(loc='upper left')
plt.grid(True, linestyle='--', alpha=0.5)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#---------------------------------------------------------------------------------------------------------------------------------------
# 5 Top Performing Suppliers 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "C:\\Users\\moon\\OneDrive\\Desktop\\project of datatool box\\Warehouse_and_Retail_Sales.csv"
df = pd.read_csv(file_path)

# Convert YEAR and MONTH into datetime for time-series plots
df['DATE'] = pd.to_datetime(df[['YEAR', 'MONTH']].assign(DAY=1))
supplier_sales = df.groupby('SUPPLIER')['RETAIL SALES'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=supplier_sales.values, y=supplier_sales.index, palette='viridis')
plt.title('Top 10 Performing Suppliers by Retail Sales', fontsize=16, fontweight='bold')
plt.xlabel('Total Retail Sales')
plt.ylabel('Supplier')
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

#------------------------------------------------------------------------------------------------------------
#-----Retail Transfers Distribution by Year----------

import pandas as pd
from statsmodels.stats.weightstats import ztest
import matplotlib.pyplot as plt
import seaborn as sns
file_path = "C:\\Users\\moon\\OneDrive\\Desktop\\Warehouse_and_Retail_Sales.csv"
df = pd.read_csv(file_path)

# Drop NA values in RETAIL TRANSFERS to avoid errors
retail_transfers = df['RETAIL TRANSFERS'].dropna()

# Hypothetical population mean (e.g., 5000)
population_mean = 5000
z_value, p_value = ztest(retail_transfers, value=population_mean)

print("Z-Test for Retail Transfers against population mean of 5000:")
print(f"Z-value: {z_value:.4f}")
print(f"P-value: {p_value:.4f}")
alpha = 0.05
if p_value < alpha:
    print("Result: Reject the null hypothesis. There is a significant difference between the sample mean and the population mean.")
else:
    print("Result: Fail to reject the null hypothesis. There is no significant difference between the sample mean and the population mean.")

# Optional visualization by year
plt.figure(figsize=(10, 6))
sns.boxplot(x='YEAR', y='RETAIL TRANSFERS', data=df, hue='YEAR',palette='coolwarm')
plt.title('Retail Transfers Distribution by Year', fontsize=16, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Retail Transfers')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

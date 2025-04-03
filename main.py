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


# creating a Scattor plot Retail V/S Warehouse Sales
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

# Creating Line graph which compare sales trends over time.
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



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
fd = "C:\\Users\\moon\\OneDrive\\Desktop\\Warehouse_and_Retail_Sales.csv"
df = pd.read_csv(fd)

# Create Pairplot (Only for Numerical Columns)
sns.pairplot(df, hue="YEAR", palette="warmcool", diag_kind="kde")

plt.show()



#-------------------------------------------------------------------------------------------------------
#Stock Movement and Retail Transfers Over Time by Item Type
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

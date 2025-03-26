import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
fd = "C:\\Users\\moon\\OneDrive\\Desktop\\Warehouse_and_Retail_Sales.csv"
data = pd.read_csv(fd)

# Counting no. of item types and their values in the dataset
item_type= data['ITEM TYPE'].value_counts() # value_counts() is used to count unique value in the column

# Creating pie chart 
plt.figure(figsize=(100, 120))  # Create a figure with the specified size
c= ['sandybrown', 'royalblue', 'navy', 'crimson', 'thistle', 'purple', 'pink']
plt.pie(item_type, labels=item_type.index, colors=c,startangle=140,autopct='%0.2f%%')
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

# Display the plot
plt.show()

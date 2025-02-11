# -*- coding: utf-8 -*-
"""ANALYSIS_OF_SUPERMARKET_SALES_DATA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1s119b1_XDbHSHAYPEh4URzTVhjPIbI0S

**ANALYSIS OF SUPERMARKET SALES DATA**
"""

#IMPORT ESSENTIAL LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
import seaborn as sns

#LOAD DATASET
df=pd.read_csv('/content/supermarket_sales - Sheet1.csv')

df.head()

"""#:: **DATA CLEANING**



"""

#CHECK FOR NULL VALUES
print(df.isnull().sum())

#CHECK FOR DUPLICATES
print(df.duplicated())

df['Date'] = pd.to_datetime(df['Date'])

print(df['Date'])

#Calculate Total Sales: Quantity * Unit Price
df['Total_Sales'] = df['Quantity'] * df['Unit price']

#Calculate Profit: Total_Sales - cogs
df['Profit'] = df['Total_Sales'] - df['cogs']

#Extract Day, Month, and Year from 'Date' for time-based analysis
df['Day'] = df['Date'].dt.day
df['Month'] = df['Date'].dt.month['Month_Name'] = df['Date'].dt.month_name()# Display the updated DataFrame
print(df)

df['Month'].dtype

"""## **DATA VISUALISATION**"""

#
top_products = df.groupby('Product line')['Total'].sum().nlargest(5).reset_index()
sns.barplot(
    data=top_products,
    x='Total',
    y='Product line',
    hue='Product line',
    palette='viridis',
    legend=False
)

#sales by branch
branch_sales = df.groupby('Branch')['Total'].sum().reset_index()
sns.barplot(data=branch_sales, x='Branch',hue='Branch', y='Total',palette='Set2')
plt.title('Sales by Branch')
plt.show()

#sales by city
city_sales = df.groupby('City')['Total'].sum().reset_index()
sns.barplot(data=city_sales, x='City',hue='City', y='Total', palette='pastel')
plt.title('Sales by City')
plt.show()

#Sales by Product Line and Gender
plt.figure(figsize=(12, 6))
sns.barplot(
    data=df,
    x='Product line',
    y='Total_Sales',
    hue='Gender',
    palette='vlag',
    estimator=sum,
    ci=None
)
plt.title('Sales by Product Line and Gender')
plt.xticks(rotation=45)
plt.xlabel('Product Line')
plt.ylabel('Total Sales')
plt.show()

#Profit Margin by Product Line
df['Profit_Margin'] = (df['Profit'] / df['Total_Sales']) * 100
profit_margin_by_product = df.groupby('Product line')['Profit_Margin'].mean().reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(
    data=profit_margin_by_product,
    x='Product line',
    y='Profit_Margin',
    palette='coolwarm'
)
plt.title('Profit Margin by Product Line')
plt.xticks(rotation=45)
plt.xlabel('Product Line')
plt.ylabel('Profit Margin (%)')
plt.show()

#Monthly Sales Trends by Product Line
monthly_sales_by_product = df.groupby(['Month', 'Product line'])['Total_Sales'].sum().reset_index()

plt.figure(figsize=(14, 8))
sns.lineplot(
    data=monthly_sales_by_product,
    x='Month',
    y='Total_Sales',
    hue='Product line',
    style='Product line',
    markers=True,
    dashes=False
)
plt.title('Monthly Sales Trends by Product Line')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.legend(title='Product Line')
plt.show()
#!/usr/bin/env python
# coding: utf-8

# # Portfolio Project: Online Retail Exploratory Data Analysis with Python

# ## Overview
# 
# In this project, you will step into the shoes of an entry-level data analyst at an online retail company, helping interpret real-world data to help make a key business decision.

# ## Case Study
# In this project, you will be working with transactional data from an online retail store. The dataset contains information about customer purchases, including product details, quantities, prices, and timestamps. Your task is to explore and analyze this dataset to gain insights into the store's sales trends, customer behavior, and popular products. 
# 
# By conducting exploratory data analysis, you will identify patterns, outliers, and correlations in the data, allowing you to make data-driven decisions and recommendations to optimize the store's operations and improve customer satisfaction. Through visualizations and statistical analysis, you will uncover key trends, such as the busiest sales months, best-selling products, and the store's most valuable customers. Ultimately, this project aims to provide actionable insights that can drive strategic business decisions and enhance the store's overall performance in the competitive online retail market.
# 
# ## Prerequisites
# 
# Before starting this project, you should have some basic knowledge of Python programming and Pandas. In addition, you may want to use the following packages in your Python environment:
# 
# - pandas
# - numpy
# - seaborn
# - matplotlib
# 
# These packages should already be installed in Coursera's Jupyter Notebook environment, however if you'd like to install additional packages that are not included in this environment or are working off platform you can install additional packages using `!pip install packagename` within a notebook cell such as:
# 
# - `!pip install pandas`
# - `!pip install matplotlib`

# ## Project Objectives
# 1. Describe data to answer key questions to uncover insights
# 2. Gain valuable insights that will help improve online retail performance
# 3. Provide analytic insights and data-driven recommendations

# ## Dataset
# 
# The dataset you will be working with is the "Online Retail" dataset. It contains transactional data of an online retail store from 2010 to 2011. The dataset is available as a .xlsx file named `Online Retail.xlsx`. This data file is already included in the Coursera Jupyter Notebook environment, however if you are working off-platform it can also be downloaded [here](https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx).
# 
# The dataset contains the following columns:
# 
# - InvoiceNo: Invoice number of the transaction
# - StockCode: Unique code of the product
# - Description: Description of the product
# - Quantity: Quantity of the product in the transaction
# - InvoiceDate: Date and time of the transaction
# - UnitPrice: Unit price of the product
# - CustomerID: Unique identifier of the customer
# - Country: Country where the transaction occurred

# ## Tasks
# 
# You may explore this dataset in any way you would like - however if you'd like some help getting started, here are a few ideas:
# 
# 1. Load the dataset into a Pandas DataFrame and display the first few rows to get an overview of the data.
# 2. Perform data cleaning by handling missing values, if any, and removing any redundant or unnecessary columns.
# 3. Explore the basic statistics of the dataset, including measures of central tendency and dispersion.
# 4. Perform data visualization to gain insights into the dataset. Generate appropriate plots, such as histograms, scatter plots, or bar plots, to visualize different aspects of the data.
# 5. Analyze the sales trends over time. Identify the busiest months and days of the week in terms of sales.
# 6. Explore the top-selling products and countries based on the quantity sold.
# 7. Identify any outliers or anomalies in the dataset and discuss their potential impact on the analysis.
# 8. Draw conclusions and summarize your findings from the exploratory data analysis.

# ## Task 1: Load the Data

# In[ ]:



import pandas as pd
df = pd.read_excel("Online Retail.xlsx")


# In[83]:



df.dtypes


# In[87]:


df.shape


# In[88]:


df.columns


# In[89]:


print(df.head(5))


# #        checking for duplicated and null values

# In[90]:



null = df.isnull().sum()       # Check for null values
null


# In[91]:


df.dropna(subset = ['Description','CustomerID'],inplace = True)       # Drop all rows with null values 


# In[92]:


null = df.isnull().sum()       # Check for null values
null


# In[94]:


df.describe()


# In[95]:


duplicate_values = df.duplicated().sum()   # check for duplicate values 
duplicate_values


# In[96]:


df.drop_duplicates(inplace = True)         #  drop all dupliacted values  


# In[97]:


duplicate_values = df.duplicated().sum()    
duplicate_values 


# In[98]:


df.shape


# #      Outlier Detection 

# In[99]:


import seaborn as sns 


# In[100]:


sns.boxplot(data = df ,x =  'Quantity')


#             Outliers Removal 

# In[101]:


for col in df.select_dtypes(include='number').columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df = df[(df[col] >= lower) & (df[col] <= upper)]


# In[102]:


df.shape


# In[103]:


df.mean()


# In[104]:


df.median()


# In[ ]:





# In[105]:


df.std()


# In[106]:


df.var()


# #      visualization 

# In[107]:


corr = df.corr()            


# In[108]:


sns.heatmap(data = corr, annot = True , cmap= 'coolwarm')


# In[110]:


top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
top_products.plot(kind='bar', figsize=(10,5), title='Top 10 Selling Products')
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[79]:


monthly_sales = df.groupby('Month')['Sales'].sum()

plt.figure(figsize=(10,6))
sns.barplot(x=monthly_sales.index, y=monthly_sales.values, palette='Blues')
plt.title("Total Sales by Month")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(range(0,12), 
           ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.show()


# In[66]:


country_sales = df.groupby('Country')['Sales'].sum().sort_values(ascending=False).head(10)
sns.barplot(x=country_sales.values, y=country_sales.index)
plt.title("Top 10 Countries by Sales")
plt.xlabel("Sales")
plt.ylabel("Country")
plt.show()


# In[82]:


df['WeekdayName'] = df['InvoiceDate'].dt.day_name()
weekday_sales = df.groupby('WeekdayName')['Sales'].sum()

# Optional: order days from Mon to Sun
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_sales = weekday_sales.reindex(weekday_order)

plt.figure(figsize=(10,6))
sns.barplot(x=weekday_sales.index, y=weekday_sales.values, palette='Greens')
plt.title("Total Sales by Day of the Week")
plt.xlabel("Day")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()


# In[67]:


df['Hour'] = df['InvoiceDate'].dt.hour
sales_by_hour = df.groupby('Hour')['Sales'].sum()

sns.barplot(x=sales_by_hour.index, y=sales_by_hour.values)
plt.title("Total Sales by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Sales")
plt.show()


# In[68]:


sales_over_time = df.resample('D', on='InvoiceDate')['Sales'].sum()
sales_over_time.plot(figsize=(12,6), title='Daily Sales Over Time')
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()


# In[ ]:





# In[ ]:





# #             feature engineering 

#        

# In[50]:


df


# In[51]:


# df.drop(['StockCode','InvoiceNo'] ,axis=1, inplace = True)      # Dropping unnecessary columns 


# In[85]:


df['Day'] = df['InvoiceDate'].dt.dayofweek
df['Hour']= df['InvoiceDate'].dt.hour
df['Month'] = df['InvoiceDate'].dt.month


# In[60]:


df['Sales'] = df['Quantity'] * df['UnitPrice']     # adding new coulmn of Total price of item


# In[63]:


df.drop('TotalPrice', axis =1, inplace=True)


# In[77]:


df


# In[ ]:





# In[ ]:





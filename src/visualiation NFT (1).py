#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

import statistics as stat


# In[3]:


data = pd.read_csv("nifty_500_quarterly_results.csv")
data


# In[4]:


data.head()


# In[5]:


data.shape


# In[6]:


data.dtypes


# In[7]:


data.describe()


# In[8]:


data.info()


# In[11]:


data.nunique()
missing_data=data.isna().sum()
perc_missingdata=(missing_data/(len(data)))*100
missing_data
perc_missingdata


# # VISUALISATION
# 

# # In this part, we are going to answer this questions:
# >1. What is the distribution of sectors and industries in the dataset?
# >2. How does revenue vary across different sectors or industries?
# >3. What is the trend in operating profit margin over time?
# >4. Is there a correlation between EPS and net profit?
# >5. Correlation between operating_expenses and operating_profit:

# ### 1. What is the distribution of sectors and industries in the dataset?

# > To answer this questions, we will use a **barplot**:
# What is a barplot, and where is it used?
# - A bar plot represents an aggregate or statistical estimate for a numeric variable with the height of each rectangle and indicates the uncertainty around that estimate using an error bar. Bar plots include 0 in the axis range, and they are a good choice when 0 is a meaningful value for the variable to take.
# - Used for categorical data.
# 
# > We used it in our case for:
# - Its simplicity and ease of interpretation make bar plots particularly suitable for displaying comparisons between different groups or categories

# In[31]:


plt.figure(figsize=(16, 14))
sns.countplot(x='sector', data=data)
plt.title('Distribution of Sectors')
plt.xlabel('Sector')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()


# ## interpretation

# ### 2. How does revenue vary across different sectors or industries?

# To answer this questions, we will use a **boxplot**:
# What is a boxplot, and where is it used?
# - A boxplot is used to compare and contrast many groups.
# - It highlights the median, and the outliers.
# - It includes the interquartile range.
# - the solid line in my boxplot refers to the median.

# In[64]:


data['revenue'] = pd.to_numeric(data['revenue'], errors='coerce')
data['profit_TTM'] = pd.to_numeric(data['profit_TTM'], errors='coerce')
data['operating_expenses'] = pd.to_numeric(data['operating_expenses'], errors='coerce')
data['operating_profit'] = pd.to_numeric(data['operating_profit'], errors='coerce')






# In[30]:


plt.figure(figsize=(20,15 ))
sns.boxplot(x='sector', y='revenue', data= data)
plt.title('Revenue Distribution Across Sectors')
plt.xlabel('Sector')
plt.ylabel('Revenue')
plt.xticks(rotation=90)
plt.show()


# Interpretation:
# > The boxplots reveal that the median Revenue **differ among the Sector**

# ### 3. What is the trend in operating profit margin over time?

# In[42]:


plt.figure(figsize=(50, 40))
sns.lineplot(x='name', y='operating_profit_margin', data=data)
plt.title('Operating Profit Margin Over Time')
plt.xlabel('Company')
plt.ylabel('Operating Profit Margin')
plt.xticks(rotation=90)
plt.yticks(rotation=90)
plt.show()


# ## 4. Is there a correlation between EPS and net profit?

# In[54]:


from scipy.stats import pearsonr
plt.figure(figsize=(40, 60))
sns.scatterplot(x='EPS', y='net_profit', data=data)
plt.title('Correlation between EPS and Net Profit')
plt.xlabel('EPS')
plt.ylabel('Net Profit')
plt.show()


# ## 5. Correlation between operating_expenses and operating_profit:

# In[68]:


from scipy.stats import pearsonr
plt.figure(figsize=(10, 8))

sns.regplot(x='operating_expenses', y='operating_profit', data=data, scatter_kws={'s': 50}, line_kws={'color': 'blue'})


plt.xlabel('operating_expenses')
plt.ylabel('operating_profit')
plt.title('Correlation between operating_expenses and operating_profit')

plt.show()


# Interpretation:
# > As operating expenses increase, operating profit tends to increase as well.
# 

# In[ ]:





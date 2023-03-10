#!/usr/bin/env python
# coding: utf-8

# Ecommerce Purchase Product

# In[2]:


import pandas as pd
data = pd.read_csv('Ecommerce Purchases.csv')
data


# In[3]:


data.head()


# In[4]:


data.head(10)


# In[5]:


data.tail(10)


# Check datatype of each column

# In[7]:


data.dtypes


# Check null values in the dataset

# In[13]:


data.isnull().sum


# In[14]:


data.columns


# In[15]:


data['Purchase Price'].max()


# In[16]:


data['Purchase Price'].min()


# How many people have french 'fr'as their language

# In[17]:


data.columns


# In[21]:


data[data['Language']=='fr']


# In[27]:


data[data['Language']=='fr'].count()


# Job Title Contain Engineer

# In[28]:


data.columns


# In[38]:


data[data['Job'].str.contains('engineer', case = False)]


# In[ ]:





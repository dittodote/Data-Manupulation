#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


reviews = pd.read_csv(r"C:\Users\slmnp\Downloads\winemag-data-130k-v2.csv\winemag-data-130k-v2.csv", index_col=0)


# In[5]:


reviews.price.dtype


# In[6]:


reviews.dtypes


# In[8]:


reviews.points.astype('float64')


# In[9]:


reviews.index.dtype


# In[12]:


reviews[pd.isnull(reviews.country)]


# In[13]:


reviews.region_2.fillna("Unknown")


# In[14]:


reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")


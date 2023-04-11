#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pd.DataFrame({'Yes': [50, 21], 'No': [131,2]})


# In[3]:


pd.DataFrame({'Bob':['I like it.','It was awful.'],'Sure':['Pretty good.','Bland.',]})


# In[4]:


pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])


# In[6]:


pd.Series([1,2,3,4,5,6])


# In[7]:


pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')


# In[12]:


wine_reviews = pd.read_csv(r"C:\Users\slmnp\Downloads\winemag-data-130k-v2.csv\winemag-data-130k-v2.csv")


# In[13]:


wine_reviews.shape


# In[14]:


wine_reviews.head()


# In[15]:


wine_reviews = pd.read_csv(r"C:\Users\slmnp\Downloads\winemag-data-130k-v2.csv\winemag-data-130k-v2.csv", index_col=0)


# In[16]:


wine_reviews.head()


# In[ ]:





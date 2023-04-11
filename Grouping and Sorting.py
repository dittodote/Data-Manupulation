#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


reviews = pd.read_csv(r"C:\Users\slmnp\Downloads\winemag-data-130k-v2.csv\winemag-data-130k-v2.csv", index_col=0)


# In[9]:


reviews.groupby('points').points.count()


# In[10]:


reviews.groupby('points').price.min()


# In[11]:


reviews.groupby('winery').apply(lambda df: df.title.iloc[0])


# In[12]:


reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])


# In[13]:


reviews.groupby(['country']).price.agg([len, min, max])


# In[14]:


countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
countries_reviewed


# In[15]:


mi = countries_reviewed.index
type(mi)


# In[16]:


countries_reviewed.reset_index()


# In[17]:


countries_reviewed = countries_reviewed.reset_index()
countries_reviewed.sort_values(by='len')


# In[18]:


countries_reviewed.sort_values(by='len',ascending=False)


# In[21]:


countries_reviewed.sort_index()


# In[23]:


countries_reviewed.sort_values(by=['country','len'])


# In[ ]:





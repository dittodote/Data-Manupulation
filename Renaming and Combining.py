#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


reviews = pd.read_csv(r"C:\Users\slmnp\Downloads\winemag-data-130k-v2.csv\winemag-data-130k-v2.csv", index_col=0)


# In[3]:


reviews.rename(columns={'points':'score'})


# In[4]:


reviews.rename(index={0:'firstEntry',1:'secondEntry'})


# In[7]:


reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')


# In[10]:


canadian_youtube=pd.read_csv(r"C:\Users\slmnp\Downloads\GBvideos.csv\GBvideos.csv")
british_youtube=pd.read_csv(r"C:\Users\slmnp\Downloads\CAvideos.csv\CAvideos.csv")
pd.concat([canadian_youtube, british_youtube])


# In[11]:


left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])

left.join(right, lsuffix='_CAN', rsuffix='_UK')


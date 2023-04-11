#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
reviews = pd.read_csv(r"C:\Users\slmnp\Downloads\winemag-data-130k-v2.csv\winemag-data-130k-v2.csv", index_col=0)


# In[1]:


pip install learntools


# In[4]:


reviews


# In[5]:


reviews.country


# In[6]:


reviews['country']


# In[11]:


reviews['country'][1]


# In[12]:


reviews.iloc[0]


# In[13]:


reviews.iloc[:,0]


# In[16]:


reviews.iloc[:3,0]


# In[18]:


reviews.iloc[1:3,0]


# In[19]:


reviews.iloc[[0,1,2],0]


# In[26]:


reviews.iloc[-5:]


# In[27]:


reviews.loc[0,'country']


# In[31]:


reviews.loc[444,'country']


# In[32]:


reviews.loc[:,['taster_name','taster_twitter_handle','points']]


# In[34]:


reviews.set_index("title")


# In[35]:


reviews.country=='Italy'


# In[36]:


reviews.loc[reviews.country=='Italy']


# In[38]:


reviews.loc[(reviews.country=='Italy')&(reviews.points>=90)]


# In[39]:


reviews.loc[(reviews.country=='Italy')|(reviews.points>=90)]


# In[40]:


reviews.loc[reviews.country.isin(['Italy', 'France'])]


# In[41]:


reviews.loc[reviews.price.notnull()]


# In[42]:


reviews['critic'] = 'everyone'
reviews['critic']


# In[43]:


reviews['index_backwards'] = range(len(reviews), 0, -1)
reviews['index_backwards']


# In[ ]:





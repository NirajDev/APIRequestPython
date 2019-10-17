#!/usr/bin/env python
# coding: utf-8

# In[11]:


import requests


# In[12]:


response = requests.get("https://api.data.gov.in/resource/6176ee09-3d56-4a3b-8115-21841576b2f6?api-key=579b464db66ec23bdd0000016007707e1fd6480a579c32b221f3c3f0&format=csv&offset=0&limit=10")


# In[13]:


response


# In[14]:


response.text


# In[ ]:





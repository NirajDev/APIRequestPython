#!/usr/bin/env python
# coding: utf-8

# In[95]:


import requests
import json
import pandas as pd


# In[96]:


headers = {'Accept': 'application/json',}
auth = ('user', 'password')
# data = {'sort_field': 'created_at','sort_direction': 'asc'}


# In[97]:


url = 'https://jungleerummy.desk.com/agent/tickets/1434536756/edit?switch_into_view=1&_=1563901012630'
response = requests.get(url, headers=headers, auth=auth)
time = []


# In[98]:


response.json()


# In[88]:


for item in data1:
       time.append(item['created_at'])
       


# In[89]:


print (time)


# In[28]:


d = re.findall('\d+-\d+-\d+',t)


# In[29]:


d


# In[30]:


import time
import datetime


# In[31]:


new_date = '2019-01-22T09:43:47Z'


# In[32]:


date_new = re.findall('\d+-\d+-\d+',new_date)


# In[35]:


print (date_new[0])


# In[36]:


unix_time = (datetime.datetime.strptime(date_new[0], "%Y-%m-%d").timestamp())


# In[37]:


unix_time


# In[ ]:





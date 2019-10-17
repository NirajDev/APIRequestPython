#!/usr/bin/env python
# coding: utf-8

# In[60]:


import play_scraper


# In[61]:


trending = play_scraper.collection(gl = 'in', collection='TRENDING', results=120,page=2)


# In[62]:


import pandas as pd
trending_data = []
for item in trending:
    trending_data.append([item['app_id'],item['url'],item['title'],item['developer'],item['score'],item['price']])

df = pd.DataFrame(trending_data, columns=["URL","Play_Store_URL","Game_Name","Company","Rating","Price"])
df.to_csv('trending_data.csv', index=False)


# In[25]:


import play_scraper
import pandas as pd
# game_collection = input('Enter Game Collection')
# game_category = input('Enter Game Category')

game_category = play_scraper.collection(gl = 'in', collection='TOP_FREE', results=120)

array = game_collection+'_data'
array = []
for item in game_category:
    array.append([item['app_id'],item['url'],item['title'],item['developer'],item['score'],item['price']])

df = pd.DataFrame(array, columns=["URL","Play_Store_URL","Game_Name","Company","Rating","Price"])
df.to_csv('TOP_GROSSING.csv', index=False)


# In[1]:


from google_play_scraper import app


# In[3]:


app.collection(category= 'app.category.GAME_ACTION')


# In[4]:


import requests


# In[5]:


res = requests.get("https://play.google.com/store/apps/top?hl=en")


# In[6]:


res.text


# In[ ]:





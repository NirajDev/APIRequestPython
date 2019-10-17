#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pytube


# In[8]:


from pytube import Playlist
pl = Playlist("https://www.youtube.com/watch?v=msXL2oDexqw&list=PLqq-6Pq4lTTbx8p2oCgcAQGQyqN8XeA1x")
title = self.player_config_args['Spring Boot Quick Start']
pl.download_all()
 # or if you want to download in a specific directory
pl.download_all('c:/Niraj')


# In[ ]:





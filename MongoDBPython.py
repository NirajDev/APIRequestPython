#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pymongo
from pymongo import MongoClient
import pandas as pd
import json
client = MongoClient('localhost', 27017)
db = client.test_database
db = client['mydatabase']
collection = db.test_collection
collection = db["17Sep"]
UserImage = [];
for obj in collection.find():
    UserImage.append([obj['_id'],obj['ID_type'],obj['UserID'],obj['Name'],obj['NameMatch'],obj['IdNumber'],obj['IdNumberMatch'],obj['DOB'],obj['DOBMatch'],obj['AutoKycStatus']])
df = pd.DataFrame(UserImage)
df.to_csv("aadhardata_17Oct.csv")


# In[4]:


import pymongo
from pymongo import MongoClient
import pandas as pd
import json
client = MongoClient('localhost', 27017)
db = client.test_database
db = client['myDb']
collection = db.test_collection
collection = db["jgOCR1"]
OCR_RESULT = [];
for obj in collection.find():
    if(obj['Comment'] is None:
       
        

    
    
    OCR_RESULT.append([obj['_id'],obj['GameId'], obj['Game_User_ID'],obj['ID_Type'],obj['OCRed_Data'],obj['Comment'],obj['Date_Added'],obj['ID_Number'],obj['Name'],obj['DOB'],obj['PIN'],obj['PAN_Match'],obj['DB_PAN']])

    
    
    
    
df = pd.DataFrame(OCR_RESULT)
df.to_csv("OCR_RESULT_2.csv")


# In[ ]:





# In[ ]:





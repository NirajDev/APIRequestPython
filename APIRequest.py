#!/usr/bin/env python
# coding: utf-8

# In[10]:


import base64
import urllib
import requests
import json
import pymongo
import os
import pandas as pd

data = pd.read_csv('C:\\Users\\niraj\\Documents\\JG-KYCStatsCheck\\static\\userdata.csv')

for i in range(0,40):
    try:
        with open(data['imagepath'][i], "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            myobj = {'inputDocument': encoded_string,'name':data['Name'][i],'idNumber':data['idNo'][i],'userID':data['UserID'][i],'idType':'PAN','dateOfBirth':data['Dob'][i]}
            data1 = urllib.parse.urlencode(myobj)
            url = 'http://localhost:8081'
            headers = {'content-type': "application/x-www-form-urlencoded",'cache-control': "no-cache"}
            response = requests.request("POST", url, data=data1, headers=headers)
#             print (response.text)
            data2 = json.loads(response.text)
            
            username = str(data['UserID'][i])
#             print (data2, str(data['filepath'][i]))
            myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            mydb = myclient["mydatabase"]
            mycol = mydb["17Sep"]
            data3 = {"ID_type":"PAN","UserID":username,
                     "Name":data2['name']['processed'],
                     "NameMatch":data2['name']['match'],
                     "IdNumber":data2['idnumber']['processed'],
                     "IdNumberMatch":data2['idnumber']['match'],
                     "DOB":data2['dateofbirth']['processed'],
                     "DOBMatch":data2['dateofbirth']['match'],
                     "AutoKycStatus":data2['autokycstatuspan']}
            mycol.insert_one(data3)
            print (i)
    except:
        print("no output received")
        

        


# In[2]:


import base64
file = input("file name\n")
with open(file, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    print (encoded_string)


# In[ ]:


# jupyter notebook --generate-config


# In[2]:


import os
for file in os.listdir("c:\\niraj"):
    print (file)


# In[3]:


import requests
response = requests.request("GET",'https://www.friendlytoyz.com/toys-on-rent.html')

response = requests.request("GET",https://www.friendlytoyz.com/toys-on-rent.html)
# In[4]:


response.text


# In[5]:


import bs4
import urllib.request


# In[6]:


webpage = urllib.request.urlopen('https://www.friendlytoyz.com/toys-on-rent.html')


# In[ ]:





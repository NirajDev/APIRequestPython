#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import requests
import boto3


# In[ ]:


aadhar = pd.read_csv('Dataset1.csv')


# In[3]:


s3 = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='')
s3.download_file('bucket', 'key', 'output_file')


# In[ ]:


import boto
import boto.s3.connection
access_key = 'key'
secret_key = 'secret'
bucket = s3.Bucket('bucket')
conn = boto.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key,
#         host = '',
        #is_secure=False,               # uncomment if you are not using ssl
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )


# In[ ]:


import boto3
import boto.s3.connection
import re
s3 = boto3.resource('s3', aws_access_key_id='key', aws_secret_access_key='secret')
bucket = s3.Bucket('bucket')
for my_bucket_object in bucket.objects.all():
#     if (re.search('pancard\/(.*)',my_bucket_object.key)):
     print (type(my_bucket_object.key))
    
    
#     if re.match(r'pan(.*)',my_bucket_object.key):
#         print (my_bucket_object.key)


# In[ ]:





# In[ ]:





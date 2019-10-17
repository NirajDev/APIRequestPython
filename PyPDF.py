#!/usr/bin/env python
# coding: utf-8

# In[5]:


import PyPDF2
pdf_obj = open('C:\\Niraj\\Projects\\Inproces\phfl\\Bank-Statement.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_obj)
if pdf_reader.isEncrypted:
    pdf_reader.decrypt('')
page = pdf_reader.getPage(4)


# In[8]:


page


# In[ ]:





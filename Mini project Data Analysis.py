#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as nm

ipl=pd.read_csv(r"C:\Users\HP\Desktop\ipl_2021_dataset.csv")


# In[3]:


ipl.head()


# In[4]:


ipl.tail()


# In[5]:


ipl.shape


# In[6]:


#Q 1 how many null values values are there in data?
ipl.isnull().sum()


# In[7]:


df= pd.DataFrame(ipl)


# In[8]:


print(df)


# In[9]:


ipl1=df.dropna()


# In[10]:


print(ipl1.to_string())


# In[11]:


# Q 2 how many duplicate values are present in this data?
print(df.duplicated().count())


# In[9]:


# sorting of base price
df.sort_values('Base Price')


# In[23]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[10]:


# Q Comparison of base price with auctioned price in dollars?
df.plot(x='Base Price',y='Cost IN $ (000)',kind="scatter",figsize=(25,4))


# In[13]:


# Q comparison of base price with auctioned price in rupees?
df.plot(x='Base Price',y='COST IN  (CR.)',kind="scatter",figsize=(25,4))


# In[12]:


# Q comparison between cost in rupees and cost in dollars
df.plot(x='Cost IN $ (000)',y='COST IN  (CR.)',kind="line",figsize=(25,4))


# In[17]:


# Q correlation between cost in dollar and cost in rupees?
df.corr()


# In[18]:


# Q Brief data information?
print(df.info())


# In[19]:


# Q 3 How many players are sold to different teams and which of them are unsold?
df['Team'].value_counts()


# In[20]:


df=df.astype({"COST IN  (CR.)":object})

df=df.astype({"Cost IN $ (000)":object})


# In[21]:


# Q 4 How many players sold above 1 crore in chennai super kings?
auction=df[df.Team=='Chennai Super Kings']
auction.head(10)
auction['Player'][auction['COST IN  (CR.)'] > 1].count()


# In[22]:


auction.head(10)


# In[ ]:





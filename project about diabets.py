#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


data = pd.read_csv('data set ofdiabetes.csv')


# In[4]:


data.head(5)


# In[5]:


data.info()


# In[35]:


data.Type.outcome.unique()


# In[26]:


data ['Type']=data ['Type'].map({'0':0;'1':1})


# In[12]:


data.head()


# In[20]:


x=data.iloc[:,[0,1,2,3,4,5,6,7]].values 

y=data.iloc[:,9].values


# In[24]:


x


# In[25]:


y


# In[21]:


from sklearn.model_selection import train_test__split
X_train, X_test, y_train, y_test= train_test__split(X,y,test_size=0.25,random_stite=0)
X_train


# In[10]:


from sklearn_processing import standered scaler
X_train=SC_X=standardscaler(X_trai)
X_test=sc_X.transform(X_test)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# **Naïve Bayes Classifier in python (Numeric data)**
# Macam MLR, Output = Y/N (numerical or categorical)

# A survey has been conducted to collect the information
# about a person will go to work by car or LRT according to
# their age and salary per month.

# 1.Gaussian NB: It should be used for features in decimal form , continuous. GNB assumes features to follow a normal distribution.
# 
# 2.MultiNomial NB: Its is used when we have discrete data (e.g. movie ratings ranging 1 and 5 as each rating will have certain frequency to represent),
# It should be used for the features with discrete values like word count 1,2,3...
# 
# 3.Bernoulli NB: It should be used for features with binary or boolean values like True/False or 0/1.

# In[1]:


#Naïve Bayes Classifier
#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import dataset
ds=pd.read_csv ('LRT_car.csv')
ds.head()


# In[2]:


ds.info()


# In[3]:


x=ds.iloc[:,:-1].values
y=ds.iloc [:,2].values
#print(x)


# In[4]:


#Naïve Bayes Classifier Step 2
#splitting the dataset into training and test sets
from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split (x, y, test_size = 0.25, random_state =0)


# In[5]:


#Naïve Bayes Classifier Step 3 (optional or depends) - to standardize
#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x_train=sc_x.fit_transform(x_train)
x_test=sc_x.transform(x_test)


# In[6]:


##Naïve Bayes Classifier Step 4
#fitting Naïve Bayes Classifier to the training set
#use GaussianNB sbb input all numerical
from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()
classifier.fit(x_train,y_train)


# In[7]:


#Naïve Bayes Classifier Step 5
#Predict the test set results
y_pred=classifier.predict(x_test)


# In[8]:


y_test, y_pred
#boleh cek berapa error, nak error low, high accuracy


# In[9]:


#Step 6 - rujuk slide 96 belah bawah kanan
#Making Confusion Matrix to check whether the test set gives the correct result
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
cm
#47+43=90 predicted correctly, 90% accuracy, already satisfied


# In[10]:


#Predict a person with salary RM6000 and 35 years old will go to work by LRT or car?
#Predict using classifier
xP=sc_x.transform ([[6000,35]])
print(xP)


# In[11]:


#classifier predict for [6000,35]
prediction= classifier.predict(xP)
print(prediction)
#answer:LRT


# Conclusion: The person with salary RM6000 and 35 years old will go to work by LRT.

# **Classification: Naïve Bayes Classifier Example (Not Numerical)**
# macam MLR, categorical data, output = Y/N

# In[12]:


#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import dataset
ds=pd.read_csv ('play.csv')
ds.head()


# In[13]:


ds.info()


# In[14]:


x=ds.iloc[:,:-1].values
y=ds.iloc [:,4].values
#case ni taknak split train n test sbb data sikit nnti jadi no accuracy.


# In[15]:


#set is to get unique data, then make it into list follow by sort
#after sort, data in sequence 0,1,2
i=0
for i in range(0,4):
    d=list(set(ds.iloc[:, i].values))
    d.sort()
    print(i,d)
    i=i+1


# In[16]:


#Handling or Encode categorical variables
from sklearn.preprocessing import LabelEncoder
labelencoder_x= LabelEncoder()
x[:, 0] =labelencoder_x.fit_transform(x[:,0])
x[:, 1] =labelencoder_x.fit_transform(x[:,1])
x[:, 2] =labelencoder_x.fit_transform(x[:,2])
x[:, 3] =labelencoder_x.fit_transform(x[:,3])
print(x)
#lepas print baru kita boleh identify, 0,1,2 tu merujuk kepada mana, refer to original table


# In[17]:


#splitting the dataset into training and test sets
from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split (x, y, test_size = 0.2, random_state =0)


# In[18]:


#STEP 3
#fitting Naïve Bayes Classifier to the dataset
#we dont use GaussianNB
from sklearn.naive_bayes import BernoulliNB
classifier=BernoulliNB()
classifier=classifier.fit(x,y)


# In[19]:


#Preidct the test set results
y_pred=classifier.predict(x_test)
y_test, y_pred


# In[20]:


#STEP 4
#Predict using classifier
#prediction=classifier.predict ([[1, 0, 0, 0]]), taknak letak decimal pun okay
prediction=classifier.predict ([[1., 0., 0., 0.]])#sunny day,cool temperature, humidity high, windy false
print(prediction)


# Conclusion: cannot play

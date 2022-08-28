#!/usr/bin/env python
# coding: utf-8

# **LOGISTIC REGRESSION - MOST ACCURATE**
# 
# Macam MLR, cuma data output dia numerical, naive bayes output dia categorical

# Given a set of data (in
# buy_car.csv ) containing information whether a person will
# buy a car base on their monthly salary and age.

# In[1]:


#Step 1
#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import dataset
ds=pd .read_csv ('buy_car.csv')
ds.head()


# In[2]:


ds.info()


# In[3]:


x=ds.iloc [:,:-1].values
y=ds.iloc [:,2].values


# In[4]:


#Step 2
#splitting the dataset into training and test sets
from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split (x, y, test_size = 0.25,
random_state = 0)


# In[5]:


#STEP 3 (OPTIONAL) FEATURE SCALLING IS FOR STANDARDIZE THE DATA
#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train=sc_x.fit_transform(x_train)
x_test=sc_x.transform(x_test) #dont need fit 


# In[6]:


#STEP 4
#fitting Logistic regression to the training set 
from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression(random_state=0)
classifier.fit(x_train,y_train)


# In[7]:


#STEP 5
#Predict the test set results
y_pred=classifier.predict(x_test)
y_pred,y_test


# In[8]:


#Making Confusion Matrix to check whether the test set gives the correct result
from sklearn.metrics import confusion_matrix
cm= confusion_matrix (y_test,y_pred)
cm


# In[9]:


#will a person with salary = 15000 and age = 21 buy the car?
y_pred_new=classifier.predict(sc_x.transform([[15000,21]]))
print(y_pred_new)


# Conclusion: The person with salary = 15000 and age = 21 will not buy the car

# **KNN - K Nearest Neighbour**

# In[10]:


#KNN-Step 1
#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import dataset
ds=pd .read_csv ('buy_car.csv')
ds.head()


# In[11]:


ds.info()


# In[12]:


#x=ds.iloc [:,[0,1]].values
x=ds.iloc [:,:-1].values
y=ds.iloc [:,2].values


# In[13]:


#KNN Step 2
#splitting the dataset into training and test sets
from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split (x, y, test_size = 0.25,
random_state = 0)


# In[14]:


#KNN-Step 3
#Feature Scaling for KNN is IMPORTANT!!! not optional okay
from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x_train= sc_x.fit_transform(x_train)
x_test=sc_x.transform(x_test)


# In[15]:


#KNN-Step 4
#fitting KNN classifier to the training set
#USE KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=5, metric='minkowski',p=2) 
#refer to using Euclidean distance
#P=2 REFER TO MINWOSKI, P=1 REFERS TO MANHATTAN?

classifier.fit(x_train,y_train)
#p : int, default=2 Power parameter for the Minkowski metric (either 1 or 2)
#can try either one of this hyper parameter
#manhattan distance is...tgk ss
#


# In[16]:


#KNN-Step 5
#Predict the test set results
y_pred=classifier.predict(x_test)


# In[17]:


#KNN-Step 6
#Making Confusion Matrix to check whether the test set gives the correct result
from sklearn.metrics import confusion_matrix
cm= confusion_matrix(y_test,y_pred)
cm
#92% accuracy (47+45)


# In[18]:


#KNN Prediction
#Will a person with with salary = 15000 and age = 21 buy the car??
y_pred_new=classifier.predict(sc_x.transform(np.array ([[15000,21]])))
print(y_pred_new)


# Conclusion: The person with with salary = 15000 and age = 21 will buy the car

# In[19]:


#Finding accuracy
from sklearn.metrics import accuracy_score
AR=accuracy_score(y_test,y_pred)
print(AR)


# **SVM -Support Vector Machine(SVM)**

# In[1]:


#SVM-Step 1
#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import dataset
ds=pd.read_csv ('buy_car.csv')
x=ds.iloc [:,:-1].values
y=ds.iloc [:,2].values


# In[2]:


#SVM-Step 2
#splitting the dataset into training and test sets
from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split (x, y, test_size = 0.25,
random_state = 0)


# In[3]:


#SVM-Step 3
#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_x =StandardScaler()
x_train= sc_x.fit_transform (x_train)
x_test =sc_x.transform (x_test)


# In[4]:


#SVM-Step 4
#fitting SVM classifier to the training set
from sklearn.svm import SVC
classifier= SVC(kernel='linear',random_state =0)#if use linear, final no. if use rbf final will be yes
classifier.fit(x_train,y_train)


# In[5]:


#SVM-Step 5
#Predict the test set results
y_pred = classifier.predict(x_test)


# In[6]:


y_pred


# In[7]:


#SVM-Step 6
#Making Confusion Matrix to check whether the test set gives thecorrect result
from sklearn.metrics import confusion_matrix
cm= confusion_matrix (y_test,y_pred)
cm


# In[8]:


#SVM-Prediction
#Will a person with salary = 15000 and age = 21 buy the car?
y_pred_new=classifier.predict(sc_x.transform(np.array([[15000,21]])))
print(y_pred_new)


# **Conclusion: The person with salary = 15000 and age = 21 will not buy the car**

# TRY TO CHANGE LINEAR TO RBF

# In[28]:


#Kernel SVM Step 4
#try to change linear to rbf
#fitting Kernel SVM classifier to the training set
from sklearn.svm import SVC
classifier= SVC(kernel='rbf', random_state =0)
classifier.fit(x_train,y_train)


# In[29]:


#Finding accuracy
from sklearn.metrics import accuracy_score
AR=accuracy_score(y_test,y_pred)
print(AR)


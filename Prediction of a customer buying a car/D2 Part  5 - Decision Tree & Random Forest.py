#!/usr/bin/env python
# coding: utf-8

# **DECISION TREE**

# In[1]:


#Decision Tree Classification-Step 1
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


# Decision Tree Classification-Step 2
#splitting the dataset into training and test sets
from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split (x, y, test_size = 0.25, random_state = 0)


# In[5]:


# Decision Tree Classification-Step 3 (no need)
#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_x =StandardScaler()
x_train =sc_x.fit_transform(x_train)
x_test =sc_x.transform(x_test)


# In[6]:


# Decision Tree Classification-Step 4
#fitting Decision Tree Classification classifier to the training set
from sklearn.tree import DecisionTreeClassifier
classifier=DecisionTreeClassifier ( criterion='entropy', random_state = 0)
classifier.fit(x_train,y_train)
#Entropy is an information theory metric that measures the impurity or uncertainty in a group of observations.
#The Gini Index or Gini Impurity is calculated by subtracting the sum of the squared probabilities of each class from one


# In[7]:


# Decision Tree Classification-Step 5
#Predict the test set results
y_pred = classifier.predict(x_test)


# In[8]:


# Decision Tree Classification-Step 6
#Making Confusion Matrix to check whether the test set gives the correct result
from sklearn.metrics import confusion_matrix
cm= confusion_matrix (y_test,y_pred)
cm
#90% accuracy (46+44)


# In[9]:


#Decision Tree Classification Prediction
#Will a person with salary = 15000 and age = 21 buy the car?
y_pred_new=classifier.predict(sc_x.transform(np.array([[15000,21]])))
print(y_pred_new)


# **Conclusion: The  person with salary = 15000 and age = 21 will not buy the car**

# In[10]:


#Finding accuracy
from sklearn.metrics import accuracy_score
AR=accuracy_score(y_test,y_pred)
print(AR)


# In[11]:


#plot tree
from sklearn import tree
from matplotlib import pyplot as plt

plt.figure(figsize=(15,15))  # set plot size (denoted in inches)
tree.plot_tree(classifier.fit(x_train,y_train),fontsize=12)
plt.show()


# **RANDOM FOREST**

# In[12]:


#Random Forest Classification-Step 1
#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import dataset
ds=pd.read_csv ('buy_car.csv')
ds.head()


# In[13]:


ds.info()


# In[14]:


#x=ds.iloc [:,[0,1]].values
x=ds.iloc [:,:-1].values
y=ds.iloc [:,2].values


# In[15]:


# Random Forest Classification-Step 2
#splitting the dataset into training and test sets
from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split (x, y, test_size = 0.25, random_state = 0)


# In[16]:


# Random Forest Classification-Step 3 (no need)
#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_x =StandardScaler()
x_train= sc_x.fit_transform (x_train)
x_test= sc_x.transform (x_test)


# In[17]:


# Random Forest Classification-Step 4
#fitting Random Forest Classification classifier to the training set
from sklearn.ensemble import RandomForestClassifier
classifier=RandomForestClassifier (n_estimators =100,criterion='entropy', random_state =0)
classifier.fit(x_train,y_train)
#Entropy is an information theory metric that measures the impurity or uncertainty in a group of observations.
#The Gini Index or Gini Impurity is calculated by subtracting the sum of the squared probabilities of each class from one


# In[18]:


# Random Forest Classification-Step 5
#Predict the test set results
y_pred =classifier.predict (x_test)


# In[19]:


# Random Forest Classification-Step 6
#Making Confusion Matrix to check whether the test set gives the correct result
from sklearn.metrics import confusion_matrix
cm= confusion_matrix (y_test,y_pred)
cm
#90% accuracy


# In[20]:


#Finding accuracy
from sklearn.metrics import accuracy_score
AR=accuracy_score(y_test,y_pred)
print(AR)


# In[21]:


#Random Forest Classification Prediction
#Will a person with salary = 15000 and age = 21 buy the car?
y_pred_new=classifier.predict (sc_x.transform (np.array ([[15000,21]])))
print(y_pred_new)


# **Conclusion: The person with salary = 15000 and age = 21 will not buy the car**

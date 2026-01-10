# !/usr/bin/env python
# coding: utf-8

# # 07-2 Predicting with machine learning

# <table class="tfo-notebook-buttons" align="left">
# <td>
# <a target="_blank" href="https://nbviewer.jupyter.org/github/rickiepark/hg-da/blob/main/07-2.ipynb"><img src="https://jupyter.org/assets/share.png" width="61" />View with Jupyter Notebook Viewer</a>
# </td>
# <td>
# <a target="_blank" href="https://colab.research.google.com/github/rickiepark/hg-da/blob/main/07-2.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />Running on Google Colab</a>
# </td>
# </table>


# Python (specialized in the study + model creation process)
# To build and service a system (requires using a framework such as tensor-flow or C, C++)


# ## Training the model
# pip install scikit-learn
# model: A software object that stores learned patterns (in scikit-learn, an instance of a class is an object)
# Result (algorithm) -> Recipe
# Supervised learning: When the correct answer (target) for each sample of data is known
# Bread (target) made with ingredients (flour, sugar) -> Can result in various results.
# input: Input is data that the model uses as material to hit the target.
# Unsupervised learning: When there is input data but no target.
# A representative example is the clustering algorithm.
# Training a model means continuously providing samples and training it to produce answers close to the correct answer.
# In[1]:


import gdown 

gdown .download ('https://bit.ly/3pK7iuu','./data/ns_book7.csv',quiet =False )


# In[2]:


import pandas as pd 

ns_book7 =pd .read_csv ('./data/ns_book7.csv',low_memory =False )
ns_book7 .head ()


# In[3]:
# In other words, when machine learning supports input values, it uses a model to automatically code and derive results.
# The key is to find out whether the sample data describes the population well.

# Python's representative machine learning package is scikit-learn, which allows you to create machine learning models.
# Functionally, one of the many cases is selected through a complex algorithm.
'''
It is more accurate to say that it is a result value made to be the same as a random number.
When training a model, taking samples, or applying shuffling to a sample, something called 'random' is used.
Applying principles is important.However, when considering ‘reproducibility’, ‘random’ means
This may be a factor that makes complete reproduction difficult.
'''
from sklearn .model_selection import train_test_split 
# Training set: 75% train_test
# Test set: 25% test_set

train_set ,test_set =train_test_split (ns_book7 ,random_state =42 )# random seed


# In[4]:
ns_book7_len =len (ns_book7 )# 376770
train_set_len =len (train_set )# 282577
test_set_len =len (test_set )# 94193
print ('ns_book7_len : ',ns_book7_len )# 376770
print ('train_set_len :',train_set_len ,round (train_set_len /ns_book7_len ,2 ))# 282577 0.75
# train_set_len : 282577 0.75
print ('test_set_len : ',test_set_len ,round (test_set_len /ns_book7_len ,2 ))# 94193 0.25
# test_set_len : 94193 0.25
print (len (train_set ),len (test_set ))# 282577 94193

# Average number of loans in each data set
ns_book7 ['대출건수'].mean ()# 11.593438968070707
train_set ['대출건수'].mean ()# 11.598732380908567
ns_book7 ['대출건수'].mean ()# 11.593438968070707

# In[5]:
# Predicting ‘number of loans’ using the ‘number of books’ column:
# Data set -> Machine learning
# Scikit-learn itself requires two-dimensional input as training data.
X_train =train_set [['도서권수']]# X is input data (data frame two-dimensional array)
y_train =train_set ['대출건수']# (Target) Answer: Series (1-dimensional)

print (X_train .shape ,y_train .shape )# (282577, 1) (282577,)
# The input, which is a two-dimensional array, lists samples in the row direction/lists the properties of the samples in the column direction.


# In[6]:
# Linear regression model (function creation) algorithm -> Setting up a formula to enter input values.
# Linear regression model: LinearRegression
from sklearn .linear_model import LinearRegression 
# Create a linear regression model
lr =LinearRegression ()
# training
lr .fit (X_train ,y_train )


# ## Evaluating the trained model: coefficient of determination

# In[7]:
# Evaluation: score()
# If the coefficient of determination is close to 1, the probability of getting the correct answer (target) increases.
# In other words, it can be seen that there is a deep relationship between the number of books and the number of loans.
X_test =test_set [['도서권수']]# input
y_test =test_set ['대출건수']# Correct answer
# Coefficient of Determination
# R**2 = 1 - (target - prediction)**2 / (target - average)**2
r2 =lr .score (X_test ,y_test )
print ("결정계수(r2): ",r2 )# Coefficient of determination (r2): 0.10025676249337057
# Result: 0.1 is not a good score
# Average means the average of the target
# When the prediction approaches the mean, the denominator and numerator become equal, and the R**2 score becomes 0.

# R² has a value between 0 and 1. The closer it is to 0, the greater the explanatory variable
# Y is said to have no degree of linear correlation, and the closer it is to 1, the greater the degree of linear correlation.

# Slope: 12.87648822
# Intercept: -3.1455454195820653
print (lr .coef_ ,lr .intercept_ )# [12.87648822] -3.1455454195820653
# In[8]:
# Predict by training the number of loans using the number of loans (y-train):
# That is, training is performed with correct answer data.
# Result: coefficient of determination 1.0
X_train2 =train_set [['도서권수']]# X is input data (data frame two-dimensional array)
y_train2 =train_set ['대출건수']# target

# Creating a linear regression model (creating an instance)
lr2 =LinearRegression ()

# Since y_train is a series object, it is converted to a two-dimensional array.
X_train2 =y_train .to_frame ()# Number of loans: training data
y_test2 =y_test .to_frame ()# Number of loans: Test data
# training
# lr2.fit(y_train.to_frame(), y_train)
# lr2.score(y_test.to_frame(), y_test) # 1.0
lr2 .fit (X_train2 ,y_train )
lr2 .score (y_test2 ,y_test )# 1.0
# ## Predicting continuous values: linear regression

# In[9]:
# Slope: 1.0
# Intercept: -1.2647660696529783e-12

print (lr .coef_ ,lr .intercept_ )





# ## Evaluate the model with mean square error and mean absolute error

# In[14]:


lr .fit (X_train ,y_train )


# In[15]:

# Prediction: Predict ‘number of loans’ using verification data
y_pred =lr .predict (X_test )

# %%
# Mean absolute error: MAE
# MAE = Sum(Absolute(Target-Prediction)) / n

from sklearn .metrics import mean_absolute_error 

mae =mean_absolute_error (y_test ,y_pred )
print (mae )# 10.358091752853873
# The result has an error similar to the average of the target.

# In[17]:

# average of target
y_test .mean ()# 11.577558841952163
# Calculate the average of the ‘number of loans’ in the population (total)
ns_book7 ['대출건수'].mean ()# 11.593438968070707
# %%

import matplotlib .pyplot as plt 

# 01: Retrieve the installed font from the specified folder and apply it to the matplotlip graph.
import matplotlib .font_manager as fm 
# font_files = fm.findSystemFonts(fontpaths=['C:/Windows/Fonts'])
font_files =fm .findSystemFonts (fontpaths =['C:/Users/Shin/AppData/Local/Microsoft/Windows/Fonts'])
for fpath in font_files :
        print (fpath )
        fm .fontManager .addfont (fpath )
plt .rcParams ['font.family']='NanumBarunGothic'

# scatterplot
fig ,ax =plt .subplots (figsize =(10 ,10 ))
ax .scatter (ns_book7 ['도서권수'],ns_book7 ['대출건수'])
ax .set_title ("도서권수 대비 대출건수")
ax .set_xlabel ("도서권수")
ax .set_ylabel ("대출권수")
fig .show ()























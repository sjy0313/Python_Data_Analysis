# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 11:18:24 2024

@author: Shin
"""
# # 07-2 Predicting with machine learning

# %%

# Machine Learning Package: Scikit-Learn
# pip install scikit-learn

import pandas as pd 

ns_book7 =pd .read_csv ('./data/ns_book7.csv',low_memory =False )
ns_book7 .head ()
# %%

from sklearn .model_selection import train_test_split 
# Training set: 75% train_test
# Test set: 25% test_set

train_set ,test_set =train_test_split (ns_book7 ,random_state =42 )# random seed


# %%

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
# %%
# training data
X_train =train_set [['도서권수']]# input
y_train =train_set ['대출건수']# Target (Correct Answer)

print (X_train .shape ,y_train .shape )# (282577, 1) (282577,)
# %%
# Verification set
X_test =test_set [['도서권수']]# data for prediction
y_test =test_set ['대출건수']# Data for correct answer
# %%
###############################################################################
# ## Predicting categories: Logistic regression (classification algorithm)
# Logistic Regression: Predicting Categories
# Category:
# - Binary classification: Divided into 2 categories, 0 or 1
# The target value has a value of True or False for some criterion.
# A collection of data corresponding to the value of the target is also called a class or label.
# - Multiclass classification: Divided into 3 or more categories
# In case of multi-classification, it belongs to single-label classification (corresponds to only one class per input value)
# - Target category: class
# - Negative class: 0
# - Positive class: 1
###############################################################################

# %%
# Average number of total loans
borrow_mean =ns_book7 ['대출건수'].mean ()
print (borrow_mean )# 11.593438968070707

# True if greater than the average number of total loans, otherwise False.

# Training Data Correct Answer
y_train_c =y_train >borrow_mean 

# Verification data correct answer
y_test_c =y_test >borrow_mean 

# %%
# Logistic Regression Model: Classification
# Binary classification that predicts whether the ‘number of loans’ is higher than the average based on the ‘number of books’
# Handled as True(1) / False(0)
from sklearn .linear_model import LogisticRegression 

# Model creation
logr =LogisticRegression ()

# training
logr .fit (X_train ,y_train_c )

# Performance measurement: accuracy
# Accuracy: Proportion of correct answers
logr .score (X_test ,y_test_c )# 0.7106154385145393
# 0.7106154385145393 Result: Approximately 71% correct
# Problem: The ratio of negative and positive classes in y_test_c is not similar.
# In[12]:

# Ratio of positive and negative classes
y_test_c .value_counts ()
'''
Number of loans
False 65337
True 28856
Name: count, dtype: int64
'''

# %%
y_test_c_len =len (y_test_c )
print ("검증세트의 건수:",y_test_c_len )# 94193

y_test_counts =y_test_c .value_counts ()
print ("True:  {}, {}".format (y_test_counts .loc [True ],y_test_counts .loc [True ]/y_test_c_len ))# 28856, 0.3063497287484208
print ("False: {}, {}".format (y_test_counts .loc [False ],y_test_counts .loc [False ]/y_test_c_len ))# 65337, 0.6936502712515792
# Voice: 69%
# Positive: 31%
# Even if you unconditionally predict the samples in X_test as the negative class, you can achieve 69% accuracy.
# %%

print ("검증세트의 건수: ",y_test_c_len )# Number of verification sets: 94193
# sklearn.dummy.DummyClassifier: Instead of considering input values, it classifies multiple
# Using classes as predictions
# DummyRegressor model predicts the average of the target.

# Dummy model: Unconditionally perform prediction with the most classes.
# Classification model

from sklearn .dummy import DummyClassifier 

dc =DummyClassifier ()
dc .fit (X_train ,y_train_c )
dc .score (X_test ,y_test_c )# 0.6936502712515792

# The result (0.6936502712515792) is equal to the negative ratio (0.6936502712515792) in the distribution of y_test_c.
# Therefore, this value becomes the reference point when creating a model.
# If the score is not at least higher than this, it cannot be considered a useful model.

# prediction
y_pred =logr .predict (X_test )# false -> 0 / true -> 1
# predicted probability
y_pred_proba =logr .predict_proba (X_test )

# %%

# Mean absolute error: MAE
# MAE = Sum(Absolute(Target-Prediction)) / n

from sklearn .metrics import mean_absolute_error 

mae =mean_absolute_error (y_test ,y_pred )
print (mae )# 11.47555550837111















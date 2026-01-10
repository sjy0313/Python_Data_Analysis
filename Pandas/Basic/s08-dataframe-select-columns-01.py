# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 15:11:09 2024

@author: Shin
"""

# Data frame: Dataframe

import pandas as pd 
# list
data =[
# 0 1 2
[15 ,'남','장안중'],# Line 0
[16 ,'여','수성중'],# Line 1 must be appended with #, so it must be an integer/slice, not a tuple.
[17 ,'여','수원대']# Line 2
]

df =pd .DataFrame (data ,index =['정윤','희애','유라'],
columns =['나이','성별','학교'])
print (df )
'''
Age Gender School
Jeongyoon 15 years old Jangan Middle School
Heeae 16 years old, Suseong Middle School
Yura 17 Female Suwon University
'''
# %%
# Index references cannot be made like series.
# KeyError: 'Jeongyun'
# print(df['Jeongyun'])

# KeyError: "None of [Index(['Jeongyun'], dtype='object')] are in the [columns]"
# print(df[['Jeongyoon']])
# %%
# Column reference: refer to all rows in the 'Age' column
# Result : series
print (df ['나이'])
'''
Jeongyoon 15
Heeae 16
Yura 17
Name: age, dtype: int64
'''
age =df ['나이']
print (age )# Series
# %%
# Column reference: refer to all rows in the 'Age' column
# Result: Dataframe
age_df =df [['나이']]
print (age_df )# Dataframe

# %%
# Multi-column reference: refer to all rows in the ‘Age’ and ‘Gender’ columns
# Result: DataFrame
age_sex =df [['나이','성별']]
print (age_sex )# Dataframe
'''
Age Gender
Jeongyoon 15 years old
Hee-ae 16 female
Yura 17 W
'''
# %%





































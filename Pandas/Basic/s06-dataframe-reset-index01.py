# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 13:52:50 2024

@author: Shin
"""

# Pandas (dataframe exists in python basic package x)
# Data frame: Dataframe
# Two-dimensional array, matrix
# row: index, row index
# Column: column, Series
# 
# form:
# df = pd.DataFrame(data[,index=index_data, columns=columns_data])
# Delete row/column

# %%
import pandas as pd 
# list
data =[
# 0 1 2
[15 ,'남','장안중'],# Line 0
[16 ,'여','수성중']# Line 1
]

df =pd .DataFrame (data ,index =['정윤','희애'],
columns =['나이','성별','학교'])
print (df )
'''
Age Gender School
Jeongyoon 15 years old Jangan Middle School
Heeae 16 years old, Suseong Middle School
'''
# %%
# reset_index()
# The index moves to the column and a new column is created.
# Index: Number is given sequentially starting from 0.
ndf =df .reset_index ()
print (ndf )
'''
index Age Gender School
0 Jeongyoon 15 M Jangan Middle School
1 Heeae 16 Female Suseong Middle School
'''
# %%
# set_index(): Move (change) the column to the index and delete the existing index.
xdf =ndf .set_index ('index')
print (xdf )
'''
Age Gender School
index
Jeongyoon 15 years old Jangan Middle School
Heeae 16 years old, Suseong Middle School
'''
# %%

xdf =ndf .set_index ('학교')
print (xdf )
'''
index age gender
school
Jangan Middle School Jeongyun 15 years old
Suseong Middle School Heae 16 F
'''
ydf =xdf .set_index ('학교')
print (ydf )
'''
Age Gender
school
Jangan Middle School 15 years old
Suseong Middle School 16 female
'''









































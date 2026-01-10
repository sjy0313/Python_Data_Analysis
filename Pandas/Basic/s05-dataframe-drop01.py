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

df =pd .DataFrame (data )
print (df )
'''
0 1 2
0 15 M Jangan Middle School
1 16 Female Suseong Middle School
'''
# %%
# Specify a new index
df .index =['정윤','희애']
'''
Age Gender School
Jeongyoon 15 years old Jangan Middle School
Heeae 16 years old, Suseong Middle School
'''
# Specify new column
df .columns =['나이','성별','학교']
print (df )
'''
Age Gender School
Jeongyoon 15 years old Jangan Middle School
Heeae 16 years old, Suseong Middle School
'''
# %%
# change index
ndf =df .rename (index ={'희애':'정희'})
print (ndf )
'''
Age Gender School
Jeongyoon 15 years old Jangan Middle School
Jeonghee, 16 years old, Suseong Middle School
'''
# Change desired column
ndf =df .rename (columns ={'학교':'중학교'})
print (ndf )
'''
Age Gender Middle School
Jeongyoon 15 years old Jangan Middle School
Heeae 16 years old, Suseong Middle School
'''
# %%

# Change original: inplace=True When you want to change multiple index or column values, use dict type + ,
# Returns: None
xdf =ndf .rename (index ={'정윤':'신정윤','희애':'신정희'},
columns ={'나이':'연령'},inplace =True )
print (ndf )
'''
Age Gender Middle School
Shin Jeong-yoon, 15 years old, Jangan Middle School
Jeonghee Shin, 16 years old, Suseong Middle School
'''
print (xdf )# None

# %%
# Axis is an element that makes up an n-dimensional array.
# Delete row: axis = 0 means row / axis = 0 means height in a 3-dimensional array
# In fact, the axis called axis = n just starts from 0 in order from the outer list to the inner list.
# It's just a name.
ndf =df .drop ('희애')
print (ndf )
'''
Age Gender School
Jeongyoon 15 years old Jangan Middle School
'''

ndf =df .drop ('희애',axis =0 )
print (ndf )
# %%

# Deleting a column: axis = 1 operates in the column direction and can be deleted by specifying an index in front of axis = 1.
ndf =df .drop ('학교',axis =1 )
print (ndf )
'''
Age Gender
Jeongyoon 15 years old
Hee-ae 16 female
'''












































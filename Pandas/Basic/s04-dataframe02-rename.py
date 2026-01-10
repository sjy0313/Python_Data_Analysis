# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 13:52:50 2024

@author: Shin
"""

# pandas
# Data frame: Dataframe
# Two-dimensional array, matrix
# row: index, row index
# Column: column, Series
# 
# form:
# df = pd.DataFrame(data[,index=index_data, columns=columns_data])

# %%
import pandas as pd 
# list
data =[
# 0 1 2
[15 ,'남','장안중'],# Line 0
[16 ,'여','수성중']# 1행      
]

df =pd .DataFrame (data ,index =['정윤','희애'],
columns =['나이','성별','학교'])
print (df )
'''
0 1 2
Jeongyoon 15 years old Jangan Middle School
Heeae 16 years old, Suseong Middle School
'''


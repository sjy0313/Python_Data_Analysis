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
[14 ,'남','수성중'],
[15 ,'남','장안중'],# Line 0
[16 ,'여','수성중'],# Line 1 must be appended with #, so it must be an integer/slice, not a tuple.
[17 ,'여','수원대']# Line 2

]

df =pd .DataFrame (data ,index =['길동','정윤','희애','유라'],
columns =['나이','성별','학교'])
print (df )
'''
Age Gender School
Gil-dong 14 South Suseong Middle School
Jeongyoon 15 years old Jangan Middle School
Heeae 16 years old, Suseong Middle School
Yura 17 Female Suwon University
'''
# %%
# Select single row
# loc: index selection
# Result: Series
ndf =df .loc ['희애']
print (ndf )# Series
'''
age 16
Gender Female
School Suseongjung
Name: Heeae, dtype: object
'''
# %%
# Select single row
# loc: index selection
# Result: Series
df2 =df .loc [['희애']]
print (df2 )# DataFrame
'''
Age Gender School
Heeae 16 years old, Suseong Middle School
'''

# %%
# Multiple row selection
# loc: Index, slicing (range designation)
# Result: Dataframe
df3 =df .loc ['정윤':'희애']
print (df3 )# Dataframe
'''
Age Gender School
Jeongyoon 15 years old Jangan Middle School
Heeae 16 years old, Suseong Middle School
'''
# %%
# Multiple row selection
# loc: Multi-index designation
# Result: Dataframe
df4 =df .loc [['정윤','희애','길동']]
print (df4 )# Dataframe
'''
Age Gender School
Jeongyoon 15 years old Jangan Middle School
Heeae 16 years old, Suseong Middle School
Gil-dong 14 South Suseong Middle School
'''

































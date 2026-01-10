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
# iloc: index selection
# Result: Series
ndf =df .iloc [1 ]
print (ndf )# Series
'''
age 15
gender guy
School Jangan Middle School
Name: Jeongyun, dtype: object
'''
# %%
# Select single row
# loc: index selection
# Result: DataFrame
df2 =df .iloc [[2 ]]
print (df2 )# DataFrame
'''
Age Gender School
Heeae 16 years old, Suseong Middle School
'''
# %%
# Multiple row selection
# iloc: slicing (range designation)
# Slicing: Start number: End number (specified up to n-1)
# Result: Dataframe
df3 =df .iloc [1 :3 ]
print (df3 )# Dataframe
'''
Age Gender School
Jeongyoon 15 years old Jangan Middle School
Heeae 16 years old, Suseong Middle School
'''
# %%
# Multiple row selection
# iloc: Multi-index designation
# Result: Dataframe extracted in specified order
df4 =df .iloc [[1 ,2 ,0 ]]
print (df4 )# Dataframe
'''
Age Gender School
Jeongyoon 15 years old Jangan Middle School
Heeae 16 years old, Suseong Middle School
Gil-dong 14 South Suseong Middle School
'''
# Ultimately, the difference between loc and iloc is whether they are specified by index or by sequence.

# %%
# Specify order and column simultaneously (using both slicing and indexing)
# Select the entire row, select 'Gender' and 'School' for the columns.
# Specify the row range and column range at the same time
df5 =df .loc [:,['성별','학교']]# loc활용 :는 행의 범위
df5 =df .iloc [:,1 :3 ]# Utilizing iloc
print (df5 )
'''
gender school
Gildong Nam Suseong Middle School
Jeong Yun Nam Jangan Middle School
Heeae Yeo Suseong Middle School
Yura Female Suwon University
'''
# %%

df6 =df .loc ['정윤':'유라',['성별','학교']]
print (df6 )
'''
gender school
Jeong Yun Nam Jangan Middle School
Heeae Yeo Suseong Middle School
Yura Female Suwon University
'''
# %%
# Rows: 1 to last -1
# Columns: 1 to last
df6 =df .iloc [1 :-1 ,1 :]# Since iloc is used as end-1, Hee-ae is designated in front of Yura.
print (df6 )
'''
gender school
Jeong Yun Nam Jangan Middle School
Heeae Yeo Suseong Middle School
'''

# %%
df7 =df .iloc [:,:]# Utilizing iloc
print (df7 )
'''
gender school
Gildong Nam Suseong Middle School
Jeong Yun Nam Jangan Middle School
Heeae Yeo Suseong Middle School
Yura Female Suwon University
'''
# %%
# entire
df8 =df .loc [:,'나이':'학교']
print (df8 )
'''
Age Gender School
Gil-dong 14 South Suseong Middle School
Jeongyoon 15 years old Jangan Middle School
Heeae 16 years old, Suseong Middle School
Yura 17 Female Suwon University
'''

























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
# dict
data ={
'c0':[1 ,2 ,3 ],# column, series (form)
'c1':[4 ,5 ,6 ],# column, series
'c2':[7 ,8 ,9 ],# column, series
'c3':[10 ,11 ,12 ],# column, series
'c4':[13 ,14 ,15 ]# column, series
}

df =pd .DataFrame (data ,index =['1행','2행','3행'])
print (type (df ))# <class 'pandas.core.frame.DataFrame'>
# ValueError: All arrays must be of the same length
# The number of rows must match the number of rows in all columns.# [1,2,3,4],(x)
print (df )
'''
c0 c1 c2 c3 c4
Line 1 1 4 7 10 13
Line 2 2 5 8 11 14
Row 3 3 6 9 12 15
'''



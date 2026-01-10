`# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:15:17 2024

@author: Shin
"""
# Pandas p152 Python webscraping complete guide

import pandas as pd 

lst =['2024-03-20',3.14 ,'ABC',100 ,True ]
# When specifying the desired index, enter the desired value in index= [], [] in the series.
sr =pd .Series (lst ,index =['날짜','원주율','알파벳','숫자','존재'])
# series basic type = pd.Series(lst[,index = index_data])
# Basic type = pd.Series(lst) # If index is not specified, index is output in 0~ integer type.
print (sr )
"""
Date 2024-03-20
Circumference ratio 3.14
Alphabet ABC
number 100
Existence True
dtype:object
"""
# Lists are specified as series values.
# Index: specified sequentially starting from 0
# Value: specified by list
# %%
# Reference index property in series
print (sr .index )# Index(['date', 'pi', 'alphabet', 'number', 'existence'], dtype='object')

# %%
# Reference value properties in a series
print (sr .values )# ['2024-03-20' 3.14 'ABC' 100 True]
# %%
# reindex(): reorder
# Specify a new index
# Create a new series without changing existing data.
sr .reindex (['존재','날짜','원주율','알파벳','숫자'])
"""
Existence True
Date 2024-03-20
Circumference ratio 3.14
Alphabet ABC
number 100
dtype:object
"""
# %%

# loc
# Reference value by index
print (sr ['원주율'])# 3.14
print (sr .loc ['원주율'])# 3.14 location

# %%

# iloc
# Refer to values ​​by sequential number
print (sr .iloc [1 ])# iloc = index location #3.14

# %%
# Not recommended. Is it explicitly accessed sequentially or sequentially?
# You must explicitly command it using sr.loc[] or sr.loc[] above.
print (sr [1 ])
# 3.14
'''
C:\Users\Shin\AppData\Local\Temp\ipykernel_10292\2091009225.py:1
: FutureWarning: Series.__getitem__ treating keys as positions is deprecated.
 In a future version, integer keys will always be treated as labels 
 (consistent with DataFrame behavior). To access a value by position, use `ser.iloc[pos]`
  print(sr[1])
'''

# %%
sr1 =pd .Series (lst ,index =[1 ,2 ,3 ,4 ,5 ])
print (sr1 )
'''
1    2024-03-20
2          3.14
3           ABC
4           100
5          True
dtype: object
'''
print (sr1 [2 ])# 3.14
print (sr1 [0 ])# KeyError: 0 # It is correct to refer to the value by index, but an error occurred.
# The index value is specified as a string, but the default value is indexed from 0 to 4.
print (sr [0 ])# 2024-03-20
# %%
# index multiple selection
print (sr ['원주율','알파벳'])
# KeyError: 'key of type tuple not found and not a MultiIndex'
print (sr [['원주율','알파벳']])# Pass it as one value to series once again with []
# tie up
'''
Circumference ratio 3.14
Alphabet ABC
dtype:object
'''

# %%
# Index multi-selection: range designation
print (sr ['원주율':'숫자'])

























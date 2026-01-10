# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:15:17 2024

@author: Shin
"""
# pandas

import pandas as pd 

# dict
dx ={'a':1 ,'b':2 ,'c':3 }

# Series: 1D
# key: index
# value: value
# index, value (composed of)
sr =pd .Series (dx )# Dictionary -> Create Pandas (Series) object
print (type (sr ),sr )# (3,)
"""
a    1
b    2
c    3
dtype: int64
"""
# %%
# Index reference in series
print (sr .index )# Index(['a', 'b', 'c'], dtype='object')
print (sr .values )# [1 2 3]

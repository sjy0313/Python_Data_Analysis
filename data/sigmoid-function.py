# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 12:01:23 2024

@author: Shin
"""

# sigmoid function
# Value between 0 and 1 (0 to 100%)
# When z is an infinitely large negative number it approaches 0
# When z is an infinitely large positive number, it approaches 1.
# Voice: p is 0.5 or less
# Positive: If p is greater than 0.5

import numpy as np 
import matplotlib .pyplot as plt 
z =np .arange (-10 ,10 ,0.1 )
p =1 /(1 +np .exp (-z ))# Calculate exponential function (e**z / e**z + 1) # To make it a value between 0 and 1

plt .plot (z ,p )
plt .xlabel ('z')
plt .ylabel ('p')
plt .show ()

# %%



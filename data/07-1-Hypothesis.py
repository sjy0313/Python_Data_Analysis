# !/usr/bin/env python
# coding: utf-8

# # 07-1 Statistical inference

# <table class="tfo-notebook-buttons" align="left">
# <td>
# <a target="_blank" href="https://nbviewer.jupyter.org/github/rickiepark/hg-da/blob/main/07-1.ipynb"><img src="https://jupyter.org/assets/share.png" width="61" />View with Jupyter Notebook Viewer</a>
# </td>
# <td>
# <a target="_blank" href="https://colab.research.google.com/github/rickiepark/hg-da/blob/main/07-1.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />Running on Google Colab</a>
# </td>
# </table>

# ## Get standard score
# Parametric test (population)
# How to estimate parameters (mean, variance) for a population in statistics
# Population refers to data of interest.
# A parametric test is to examine some samples selected from the population and then estimate the mean.
# Parametric tests are often performed on the assumption that population data follows a normal distribution.
# Although we don't actually know the entire data, data in the natural world follows a normal distribution.
# %%
# [Cumulative distribution]
# Standard Normal Distribution Normal distribution with mean 0 and standard deviation 1
# Substituting the mean of 0 and standard deviation of 1 into the z-score formula, z = x
# Use z-scores to show how overall data is distributed

# %%
# Assume that the data follows a normal distribution
# A standard score is a score converted using standard deviation to determine how far each value is from the mean.
# Standard score -> z-score
# The larger the standard score, the further the distance from the mean.
# In the standard normal distribution, samples with z scores within 1.0 account for 68% of the total.
# In the standard normal distribution, samples with z-scores within 2.0 account for 95% of the total.
from scipy import stats 
# Python function stats.norm.cdf(z) to find cumulative distribution
stats .norm .cdf (0 )# 0.5 -> 50% interval average
stats .norm .cdf (1.0 )-stats .norm .cdf (-1.0 )# 0.6826894921370859 -> 68%
stats .norm .cdf (2.0 )-stats .norm .cdf (-2.0 )# 0.9544997361036416 -> 95%
# Python function to find z-score with cumulative distribution:
stats .norm .cdf (0 )

# In[1]:
# Find standard score

import numpy as np 

x =[0 ,3 ,5 ,7 ,10 ]

s =np .std (x )# standard deviation
m =np .mean (x )# average
z =(7 -m )/s # 7 selected from the standard score population - mean / std = 0.5872202195147035
print (z )# 0.5872202195147035
# %%
print ("표준편차: ",s )# Standard Deviation: 3.40587727318528
print ("평균: ",m )# Average: 5.0
# %%

zs =[]
for n in x :
    z =(n -m )/s 
    zs .append .round (z ,8 )

print (zs )# [-1.4680505487867588, -0.5872202195147035, 0.0, 0.5872202195147035, 1.4680505487867588]

# In[2]:

# Use of Sci-Fi
# conda activate YSIT24
# pip install scipy
from scipy import stats 

stats .zscore (x )# array([-1.46805055, -0.58722022, 0. , 0.58722022, 1.46805055])


# In[3]:

# Python function stats.norm.cdf(z) to find cumulative distribution
stats .norm .cdf (0 )# 0.5


# In[4]:

# Python function stats.norm.cdf(z) to find cumulative distribution
stats .norm .cdf (1.0 )-stats .norm .cdf (-1.0 )# 0.6826894921370859 -> 68%


# In[5]:

# Python function stats.norm.cdf(z) to find cumulative distribution
stats .norm .cdf (2.0 )-stats .norm .cdf (-2.0 )# 0.9544997361036416 -> 95%


# In[6]:

# Python function to find z-score with cumulative distribution:
stats .norm .ppf (0.9 )# 1.2815515655446004
# Python function to find z-score with cumulative distribution:
stats .norm .ppf (0.95 )# 1.6448536269514722
# Python function to find z-score with cumulative distribution:
stats .norm .ppf (0.68 )# 0.4676987991145084



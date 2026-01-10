# -*- coding: utf-8 -*-
'''
Created on Wed Apr  3 15:31:46 2024

@author: Shin
'''

# ## Learn about the central limit theorem
# “The mean of a randomly selected sample is close to a normal distribution.”
# What data does not follow the standard normal distribution?
# The central limit theorem is used as a method to derive normal distribution characteristics.
# The process of calculating the average of samples randomly selected from the population is repeated several times.
# If you calculate the average and transfer the values ​​of these averages to a histogram, it follows a normal distribution.
# histogram
# A histogram is an important tool for visually representing the distribution of data.
# This chart summarizes large amounts of data and indicates the frequency of values.
# Therefore, it helps in determining data distribution trends and medians.
# It's also effective at highlighting gaps and outliers in your data.

# %%
'''
Population Variance:

Population variance represents the variance of the population.Population refers to the entire group of people you wish to analyze.
Population variance is calculated as the average of the squares of the deviations between all individual data points and the population mean.
Population variance is used to describe the characteristics of a population.However, it is realistic to survey the entire population
may not be possible.
Sample Variance:

Sampling variance refers to the variance of a sample data set.A sample refers to a subset drawn from a population.
Sampling variance is calculated as the average of the squares of the deviations between each individual data point and the sample mean.
Sampling variance is used to estimate population characteristics.Similar to the population variance, but
Because it is calculated from a sample, it may not exactly match the true variance in the population.
Sampling variance plays an important role in statistical inference and hypothesis testing.
Therefore, population variance represents the characteristics of the population, and sample variance is based on sample data.
It is used to estimate characteristics of a population.Sample variance is used for more realistic and practical analysis.
It is used to estimate characteristics of a population.
'''


# %%


# In[7]:


import gdown 

gdown .download ('https://bit.ly/3pK7iuu','./data/ns_book7.csv',quiet =False )


# In[8]:


import pandas as pd 

ns_book7 =pd .read_csv ('./data/ns_book7.csv',low_memory =False )
ns_book7 .head ()


# In[9]:


import matplotlib .pyplot as plt 
# Histogram of number of loans
plt .hist (ns_book7 ['대출건수'],bins =50 )
plt .yscale ('log')# log scale
plt .show ()


# In[10]:
import numpy as np 

np .random .seed (42 )# Specify initial value for pseudo-random number generation
# Calculate the average of the ‘number of loans’ by sampling 30 cases out of 1000.
sample_means =[]
for _ in range (1000 ):
    m =ns_book7 ['대출건수'].sample (30 ).mean ()
    sample_means .append (m )


    # In[11]:

    # Although left-right symmetry is not perfect, a bell-shaped distribution is formed.
plt .hist (sample_means ,bins =30 )
plt .show ()


# In[12]:
# Magic number: 30
# Calculate the average of the ‘number of loans’ by sampling 30 cases out of 1000.
# Grand average of sample data
np .mean (sample_means )# 11.539900000000001


# In[13]:


ns_book7 ['대출건수'].mean ()# 11.593438968070707


# In[14]:

# Calculate the average of the ‘number of loans’ by sampling 20 cases out of 1,000.
np .random .seed (42 )
sample_means =[]
for _ in range (1000 ):
    m =ns_book7 ['대출건수'].sample (20 ).mean ()
    sample_means .append (m )
np .mean (sample_means )
# Closer to the average (11.5934) of the ‘number of loans’ in the population (total).
np .mean (sample_means )# 11.39945
# %%
# Calculate the average of the ‘number of loans’ by sampling 50 cases out of 1000.
np .random .seed (42 )
sample_means =[]
for _ in range (1000 ):
    m =ns_book7 ['대출건수'].sample (50 ).mean ()
    sample_means .append (m )
np .mean (sample_means )# 11.53212
# %%
# Calculate the average of the ‘number of loans’ by sampling 60 cases out of 1000.
np .random .seed (42 )
sample_means =[]
for _ in range (1000 ):
    m =ns_book7 ['대출건수'].sample (60 ).mean ()
    sample_means .append (m )
np .mean (sample_means )# 11.511583333333332
# %%
# Calculate the average of the ‘number of loans’ by sampling 40 cases out of 1000.
np .random .seed (42 )
sample_means =[]
for _ in range (1000 ):
    m =ns_book7 ['대출건수'].sample (40 ).mean ()
    sample_means .append (m )
np .mean (sample_means )# 11.5613
# %%
# ns_book7 population
# Average value according to the number of samples
# Total: 11.593438968070707
# 20 cases: 11.39945
# 30 cases: 11.539900000000001
# 40 cases: 11.5613 # 40 cases is closest to the total
# 50 cases: 11.53212
# 60 cases: 11.511583333333332
# In[16]:

# standard deviation of the mean of the sample (40)
np .std (sample_means )# 3.0355987564235165


# In[17]:
# Standard Error
# The population mean is unknown, and the z-score formula for the sample mean is:
# z = (14.75 - population mean) / (standard deviation of sample mean)
# Standard deviation of sample mean = standard deviation of population / square root (number of samples included in sample)
np .std (ns_book7 ['대출건수'])/np .sqrt (40 )# 3.048338251806833
print (np .std (ns_book7 ['대출건수']))# 19.27938390865096
print (np .sqrt (40 ))# 6.324555320336759

# Confidence Interval
# ## Estimate the mean range of a population: confidence interval
# Prerequisites:
# If we have just one sample, can we estimate the population mean?
# A confidence interval is the range of a population parameter within which the sample parameter (mean) is believed to fall.

# In[18]:
# Calculate the confidence interval using the number of loans for the ‘Python’ book.
# The first character of the 'subject classification number' starts with 00 and the book name includes Python.
python_books_index =ns_book7 ['주제분류번호'].str .startswith ('00')&ns_book7 ['도서명'].str .contains ('파이썬')
python_books =ns_book7 [python_books_index ]
python_books .head ()

# In[19]:


len (python_books )# 251 cases


# In[20]:

# Average number of loans for Python books
python_mean =np .mean (python_books ['대출건수'])
python_mean # 14.749003984063744


# In[21]:

# Standard error of central limit theorem
# Standard Error
# Standard deviation of sample mean = standard deviation of sample / square root (number of samples included in sample)
python_std =np .std (python_books ['대출건수'])
python_se =python_std /np .sqrt (len (python_books ))
python_se # 0.8041612072427442


# In[22]:
# Cumulative distribution z-score
from scipy import stats 
# 0.975 = 1 - 0.025
# 2.5% sections on each side of the 95% area centered on the average
stats .norm .ppf (0.975 )# 1.959963984540054


# In[23]:


stats .norm .ppf (0.025 )


# In[24]:

# Average number of loans for Python books
python_mean =np .mean (python_books ['대출건수'])
python_mean # 14.749003984063744

# Assume that the standard deviation of the population is similar to the standard deviation of the sample.
# Instead of the standard deviation of the population, the number of Python books loaned at Namsan Library, which can be considered a sample,
# If you find the standard deviation and then find the standard error,
# Standard error of central limit theorem (standard mean of sample mean)
python_se # 0.8041612072427442


# Population average ('Number of loans'): 11.593438968070707
# Based on the sample mean python_mean value and standard error python_se, the population mean is

# 95% confident it will lie between 13.2 and 16.3
# At a 95% confidence interval, the population mean of Python books lies between 13.2 and 16.3.

# Guess the population mean (sample mean)
print (python_mean -1.96 *python_se ,python_mean +1.96 *python_se )
# 13.172848017867965 16.325159950259522
# It is assumed to lie between 13.2 and 16.3.


# ## Checking statistical significance: Hypothesis testing
# Hypothesis test hypothesis test p397/ permutation test p 402
# Null hypothesis or null hypothesis
# This is a hypothesis if there are no teeth or there is no meaningful difference, and it is either true or false.
# This is a hypothesis that is intended to be proven through statistical evidence.
# -Hypothesis expected to be statistically insignificant between samples
# -H0
# -Books: The average number of loans for Python and C++ books is the same.
# alternative hypothesis
# -Ha
# -Hypothesis: The average number of loans for Python and C++ books is not the same.
# -
# Significance level
# - 0.05(5%), 0.01(1%)
# - The commonly used standard is the point where the area of ​​both tails of the normal distribution adds up to 5%.
# - When the p-value is less than 0.05%, the null hypothesis is rejected and the alternative hypothesis that becomes true is the alternative hypothesis.
# - The standard for z-score is the significance level.
# Significance Probability (p-value)
# -Establish null hypothesis (H0) and alternative hypothesis (Ha)
# -Select appropriate statistics: z-statistic, t-statistic
# -p-value calculation


# z-score (standard score: data points on a normal distribution) for the average of two populations
# Ratio that represents the ratio of the standard deviation of how far away from the origin)
# z = ((x1-x2) - (u1-u2)) / sqrt((s2**2/n1) + (s2**2/n2))
# x1: Mean of samples in Python / x2: Mean of samples in C++
# u1: Mean of the population in Python / u2: Mean of the population in C++
# s1: Standard deviation (standard error) of Python sample / s2: Standard deviation (standard error) of C++ sample
# n1: Number of Python samples / n2: Number of C++ samples

# Standard Error
# Quantifying the uncertainty about the estimate of the average
# An indicator of how close the sample mean is to the population mean.
# The error of sample mean is the deviation of the sample mean from the population mean.
# -Formula: Standard deviation of sample = Standard deviation of population / square root (number of samples included in the sample)
# -The standard deviation of the sample and the standard deviation of the population are almost identical (similar).

# Since a random sample is drawn from the population and the mean of the random sample is unknown, the standard deviation of the population is borrowed.
# Estimate the average assuming they are similar.
# Let's assume that there are random samples from x1 to x5 and that the sum of these values ​​is 100.
# Without knowing each value of the random sample, I tried to set the values ​​of x1 to x5 not to exceed 100.
# Four of the five x (random sample) values ​​are free, while one x value exists to set 100.
# It is not free. In this case, the degree of freedom is 4.
# Therefore, when calculating the standard deviation of the sample mean, divide by sample-1, which is one less than the number of samples, to obtain the standard deviation of the sample.



# Our goal is to determine the significance of the null hypothesis (i.e., whether it is true or not true) based on the collected sample data.
# It is a test. If the null hypothesis is true, it means that it is not statistically significant, and it is false.


# %%
# regex=False Reason:
# This is because the default behavior is for the str.contains method to use regular expressions to perform pattern matching.
# However, in this case no regular expression is needed, simply the string
# You just need to check if it is included in another string, so use regex=False
cplus_books_index =ns_book7 ['주제분류번호'].str .startswith ('00')&ns_book7 ['도서명'].str .contains ('C++',regex =False )
cplus_books =ns_book7 [cplus_books_index ]
cplus_books .head ()


# In[26]:

python_mean =np .mean (python_books ['대출건수'])
python_mean # 14.749003984063744
len (cplus_books )# 89


# In[27]:
import numpy as np 
# Average of a sample: c++
cplus_mean =np .mean (cplus_books ['대출건수'])
cplus_mean # 11.595505617977528


# In[28]:

# Standard-Error
cplus_se =np .std (cplus_books ['대출건수'])/np .sqrt (len (cplus_books ))
cplus_se # 0.9748405650607009


# In[29]:
# python_mean: 14.749003984063744
# cplus_mean: 11.595505617977528
# python_se : 0.8041612072427442
# cplus_se : 0.9748405650607009

# z-score:
pc_z_score =(python_mean -cplus_mean )/np .sqrt (python_se **2 +cplus_se **2 )
pc_z_score =round (pc_z_score ,2 )
print (pc_z_score )# 2.5

# In[30]:
# Cumulative Bupo: 0.9937903346742238
from scipy import stats 

# stats.norm.cdf(2.50) # 0.9937903346742238
pc_norm_cdf =stats .norm .cdf (pc_z_score )
pc_norm_cdf =round (pc_norm_cdf ,3 )
print (pc_norm_cdf )# 0.994

# In[31]:


p_value =(1 -0.995 )*2 
p_value # 0.010000000000000009
# %%
p_value =(1 -pc_norm_cdf )*2 
p_value # 0.01200000000000001
# %%
# Result: Reject the null hypothesis: There is a difference in the means of Python and C++ books.
# True = p_value(0.012) < p_level(0.05)
p_level =0.05 
p_tf =p_value <p_level 
print (p_tf )# True

# In[32]:
# Testing a Hypothesis with a t Test ttest_ind()
# Perform a t-test to compare two t-distributed samples. The t-distribution is similar to the normal distribution, but
# The center is slightly lower and the tail is thicker.# t-distribution when the sample size is less than 30
# Recommended to use.

# You can use this function to compare means regardless of sample size.##

# If you input the data from the Python/C++ book obtained earlier into ttest_ind, the t-score and p-value are returned.

t ,pvalue =stats .ttest_ind (python_books ['대출건수'],cplus_books ['대출건수'])
print (t ,pvalue )# 2.1390005694958574 0.03315179520224784
# 0.03315179520224784 p value
t_value =0.03315179520224784 
t_tf2 =t_value <p_level 
print (t_tf2 )# True
# Therefore, the null hypothesis is rejected, and the difference in the average number of loans for the two books is not a coincidence.

# All of the above processes were carried out under the assumption that the population mean follows a normal distribution.

# (Estimating the parameters (mean, variance) of the population x -> nonparametric-test)
# Testing a hypothesis when the distribution is not normal: permutation test
# When the distribution of the population is not normal or the distribution of the population is unknown.
# Calculate the difference between the means in the two groups again
# Repeat the above process several times
# The mean difference in the original sample is greater than the mean difference in the randomly divided groups.
# Calculate p-value by counting large or small cases
# In[33]:

# First, create a statistical function that receives two arrays and calculates the average.
def statistic (x ,y ):
    return np .mean (x )-np .mean (y )


    # In[34]:

    # Permutation test execution function:
    # After combining two arrays with numpy.append(), use permutation to randomly extract them.
    # The two groups are made equal to the size of the original sample. (Number of samples in two groups = Number of population samples)
    # Create a randomly shuffled array and generate a random index equal to the entire array length.
    # Divide into two groups with x_ and y_ as indices and calculate the average difference between groups.
    # Repeat this 1000 times

def permutation_test (x ,y ):
# Calculate the difference between the sample means.
    obs_diff =statistic (x ,y )
    # Combine the two samples.
    all =np .append (x ,y )
    diffs =[]
    np .random .seed (42 )
    # Repeat the permutation test 1000 times.
    for _ in range (1000 ):
    # Shuffle the entire index.
        idx =np .random .permutation (len (all ))
        # Randomly divide them into two groups and then calculate the mean difference.
        x_ =all [idx [:len (x )]]
        y_ =all [idx [len (x ):]]
        diffs .append (statistic (x_ ,y_ ))
        # Calculate the p-value for cases that are smaller or larger than the original sample.
    less_pvalue =np .sum (diffs <obs_diff )/1000 
    greater_pvalue =np .sum (diffs >obs_diff )/1000 
    # Choose the smaller p-value of the two and multiply it by 2 to return the final p-value.
    return obs_diff ,np .minimum (less_pvalue ,greater_pvalue )*2 


    # In[35]:
print (['대출건수'])
print (python_books ['대출건수'])# 251
print (cplus_books ['대출건수'])# 89
# This is the total number of loans in the population, and the target of the sample was books with python in the title.
# At this time, the sample mean, that is, Python is included, and the average number of books borrowed is calculated with np.mean().
# def statistic(x, y):
# return np.mean(x) - np.mean(y)
# Above, we created a function that calculates the average of the two values ​​x and y.
# obs_diff = statistic(x,y) was defined.This refers to the difference between the two sample means.

np .mean (ns_book7 ['대출건수'])# 11.593438968070707 # Average number of loans in the population
np .mean (python_books ['대출건수'])# 14.749003984063744 # Average number of python books loaned
np .mean (cplus_books ['대출건수'])# 11.595505617977528 # Average number of C++ books loaned



pm_test =permutation_test (python_books ['대출건수'],cplus_books ['대출건수'])
print (pm_test )# (3.1534983660862164, 0.022)

# Difference between the means of the two groups: 3.1534983660862164
# p-value: 0.022

# Result p-value(0.022) < less than 0.05
# Since it does not meet the significance level, the null hypothesis is rejected.
# It can be seen that there is a difference in the average number of loans for the two books.

# In[36]:


# It only runs on scipy 1.8 or higher.
res =stats .permutation_test ((python_books ['대출건수'],cplus_books ['대출건수']),
statistic ,random_state =42 )
p_value =0.0258 
# The result is approximately 3.153 0.0258.
print (res .statistic ,res .pvalue )# 3.1534983660862164 0.0258

res1 =stats .permutation_test ((python_books ['대출건수'],cplus_books ['대출건수']),
lambda x ,y :np .mean (x )-np .mean (y ),random_state =42 )
'''
random_state:

It is mainly used in the machine learning library scikit-learn.
Most models in scikit-learn have a random_state parameter.
'''
# In[36]:

# ['Topic classification number'].str.startswith('00') is a condition that the subject classification number starts with 00.
java_books_indx =ns_book7 ['주제분류번호'].str .startswith ('00')&ns_book7 ['도서명'].str .contains ('자바스크립트')
java_books =ns_book7 [java_books_indx ]
java_books .head ()


# In[37]:
# Python average number of loans: python_mean = np.mean(python_books['Number of loans'])
python_mean # 14.749003984063744
# Average number of java loans out of 105 books:
print (len (java_books ),np .mean (java_books ['대출건수']))# 105 15.533333333333333


# In[38]:


permutation_test (python_books ['대출건수'],java_books ['대출건수'])# (-0.7843293492695889, 0.566)
# result
# p_value(0.566) is greater than 0.05
p_value =0.566 
p_value <0.5 
print (p_value )
# The null hypothesis cannot be rejected

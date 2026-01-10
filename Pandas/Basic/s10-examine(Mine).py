# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:52:16 2024

@author: Shin
"""

# problem
# Find the total score and average using a data frame.
# 1. Specify ‘name’ as the index
# 2. Total score and average for each student
# 3. Total score and average for each subject
# 4. Compose the processing results into one new frame
#
# Example result:
# Name Math English Music Physical Education Total Score Average
# Seojun 90 98 85 100 373 93
# Junseo 90 98 85 100 373 93
# Ina 90 98 85 100 373 93
# Mercury 90 98 85 100 373 93
# Total score 360 ​​392 100 400 0 0
# Average 90 98 80 100 0 0
# condition:
# 1. Use loops
# 2. Read and process each row and column one by one
# %%
import pandas as pd 
# list

score =[
[90 ,98 ,85 ,100 ],
[90 ,98 ,85 ,100 ],
[90 ,98 ,85 ,100 ],
[90 ,98 ,85 ,100 ],
]

df =pd .DataFrame (score ,columns =['수학','영어','음악','체육'],
index =['서준','준서','인아','수성'])
print (df )
# Create an empty index (row)
ndf =df .reset_index ()
print (ndf )
# 'index
# See s04-dataframe-index-column01.py, s06-dataframe-reset-index01.py
ndf .rename (columns ={'index':'이름'},inplace =True )# change original
print (ndf )
pdf =ndf .set_index ('이름')
print (pdf )

# Total score for each student
df ['총합']=pdf .sum (axis =1 )
print (df )

# %%
# Full designation
df3 =df .loc [:,['수학','영어','음악','체육']]
print (df3 )
df2 =df .iloc [:,:4 ]
print (df2 )
# df2 = df3
# %%

# series form
df4 =df2 .iloc [0 ]
print (df4 )
'''
math 90
English 98
music 85
PE 100
Name: Seojun, dtype: int64
'''
# Reference value, which is the property value in the series.
print (df4 .values )
# [90 98 85 100]
# When referring to the value of one element, you can change it to series and then refer to the attribute value.
# When checking multiple property values
df .columns # Index(['Math', 'English', 'Music', 'Physical Education'], dtype='object')
df .index # Index(['Seojun', 'Junseo', 'Ina', 'Suseong'], dtype='object')
# %%

# Finding totals and averages with loops
# total
score1 =[90 ,98 ,85 ,100 ]
total =[sum (score1 )for score1 in score ]
print (total )

# Total by subject
# Example result:
# Name Math English Music Physical Education Total Score Average
# Seojun 90 98 85 100 373 93
# Junseo 90 98 85 100 373 93
# Ina 90 98 85 100 373 93
# Mercury 90 98 85 100 373 93
# Total score 360 ​​392 100 400 0 0
# Average 90 98 80 100 0 0

# math total
math =df .iloc [:,0 ]
print (math .values )
# [90 90 90 90]
tmath =sum (math .values )
print (tmath )# 360

# English total
english =df .iloc [:,1 ]
print (english .values )
tenglish =sum (english .values )
print (tenglish )# 392

# average:
score1 =[90 ,98 ,85 ,100 ]
avg =[sum (score1 )/len (score1 )for score1 in score ]
print (avg )

# average by subject
# %%

ndf ['총점']=0 
ndf ['평균']=0 
# Add row
ndf .loc ['평균']=0 
print ("#학생별 총점 및 평균#")
for x in range (len (ndf )):
    rows =ndf .iloc [x ,:]
    tot =0 
    for val in rows :
        tot +=val 
    ndf .iloc [x :4 ]=tot 
    ndf .iloc [x ,5 ]=tot //cnt 








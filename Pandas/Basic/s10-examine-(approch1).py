# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 17:29:09 2024

@author: Shin
"""
# 2023/3/21
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


exam_data ={'이름':['서준','우현','인아'],
'수학':[90 ,80 ,70 ],
'영어':[98 ,89 ,95 ],
'음악':[85 ,95 ,100 ],
'체육':[100 ,90 ,90 ]}
df =pd .DataFrame (exam_data )
print (df ,'\n')

# %%
# Specify 'name' as index
ndf =df .set_index ('이름')
print (ndf )
# sr = ndf.loc[:,'Math':'Physical Education'] # Check all rows and all columns by creating a new data frame
sr =ndf .loc [:,:]# Check all rows and all columns by creating a new data frame
print (sr )

# %%
# Total score for each student
cnt =len (ndf .columns )
print ("과목건수: ",cnt )

# Add column
ndf ['총점']=0 
ndf ['평균']=0 
print (ndf )

# %%
print ("# 학생별 총점 및 평균 #")
for x in range (len (ndf )):# number of rows
    rows =ndf .iloc [x ,:]# extract one row
    tot =0 
    for val in rows :# Accumulated by searching one column at a time
        tot +=val 
    ndf .iloc [x ,4 ]=tot # total score
    ndf .iloc [x ,5 ]=tot //cnt # average

print (ndf )






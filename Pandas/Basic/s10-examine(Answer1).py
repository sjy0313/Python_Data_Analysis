# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 17:26:48 2024

@author: Shin
"""
# -*- coding: utf-8 -*-

import pandas as pd 

# Convert a data frame with the DataFrame() function.Save to variable df
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
    ndf .iloc [x ,5 ]=tot //cnt # 평균

print (ndf )

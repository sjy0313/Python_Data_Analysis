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
#
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

pdf =ndf .set_index ('이름')
print (pdf )


xdf =ndf .rename (index ={'정윤':'신정윤','희애':'신정희'},
columns ={'나이':'연령'},inplace =True )
print (ndf )






'총점','평균'
print (df )



score =[90 ,98 ,85 ,100 ]
total =0 
for sc in range (4 ):
   total +=score [sc ]
print (total )
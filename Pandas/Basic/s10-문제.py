# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 17:15:10 2024

@author: Shin
"""

# %%
"""
[Problem] Find the total score and average using the data frame below.
1. Specify ‘name’ as the index
2. Total score and average for each student
3. Total score and average for each subject
4. Organize the entire thing into one new data frame
"""

"""
[Result] Example, average (integer)
# Total score and average for each subject #
Math English Music Physical Education Total Score Average
name
Seojun 90 98 85 100 373 93
Starboard 80 89 95 90 354 88
Ina 70 95 100 90 355 88
Total score 240 282 280 280 0 0
Average 80 94 93 93 0 0
"""

# %%
import pandas as pd 

# Convert a data frame with the DataFrame() function.Save to variable df
exam_data ={'이름':['서준','우현','인아'],
'수학':[90 ,80 ,70 ],
'영어':[98 ,89 ,95 ],
'음악':[85 ,95 ,100 ],
'체육':[100 ,90 ,90 ]}
df =pd .DataFrame (exam_data )

print (df )

print (df ,sep ='\n')

# print('\n')
'''
Moves to the next line, also called newline.
print('\n') prints a blank line.where \n represents the newline character.
Therefore, print('\n') only moves the cursor and prints a blank line, with nothing on the new line.
This allows you to organize the output results nicely.
#
When you want to display multiple output results in one line
print(1, end=' ') # Specify a space at end
print(2, end=' ')
print(3)
# 1 2 3
'''
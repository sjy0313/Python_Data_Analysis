# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 15:11:09 2024

@author: Shin
"""

# Data frame: Dataframe

import pandas as pd 
# list
data =[
# 0 1 2
[15 ,'남','장안중'],# Line 0
[16 ,'여','수성중'],# Line 1 must be appended with #, so it must be an integer/slice, not a tuple.
[17 ,'여','수원대']# Line 2
]

df =pd .DataFrame (data ,index =['정윤','희애','유라'],
columns =['나이','성별','학교'])
print (df )
'''
Age Gender School
Jeongyoon 15 years old Jangan Middle School
Heeae 16 years old, Suseong Middle School
Yura 17 Female Suwon University
'''

# %%
# Save file
# Default: index=True, header=True, sep=' ')
df .to_csv ("./학생성적.txt")

# Saved results: student grades.txt
'''
,age, gender, school
Jeongyoon, 15, male, Jangan Middle School
Heeae, 16, female, Suseong Middle School
Yura, 17, female, Suwon University
'''
df .to_csv ("./학생성적-noindex.txt",index =False )
# Saved results: student grades-noindex.txt
'''
Age, gender, school
15, Male, Jangan Middle School
16, female, Suseong Middle School
17, female, Suwon University
'''
# %%

ndf =df .reset_index ()
ndf .rename (columns ={'index':'이름'},inplace =True )
ndf .to_csv ("./학생성적-index-이름.txt",index =False )
# Saved results: student grades-index-column.txt
'''
Name, age, gender, school
Jeongyoon, 15, male, Jangan Middle School
Heeae, 16, female, Suseong Middle School
Yura, 17, female, Suwon University
'''

# %%
# Read the file saved above
rdf =pd .read_csv ("./학생성적-index-이름.txt")
rdf .set_index ('이름',inplace =True )
print (rdf )
'''
Age Gender School
name
Jeongyoon 15 years old Jangan Middle School
Heeae 16 years old, Suseong Middle School
Yura 17 Female Suwon University
'''
# %%

odf =pd .read_csv ("./학생성적.txt")
print (odf )
'''
Unnamed: 0 Age Gender School
0 Jeongyoon 15 M Jangan Middle School
1 Heeae 16 Female Suseong Middle School
2 Yura 17 Yeo Suwon National University
'''
odf .rename (columns ={'Unnamed: 0':'이름'},inplace =True )# inplace=True change original
print (odf )
'''
Name Age Gender School
0 Jeongyoon 15 M Jangan Middle School
1 Heeae 16 Female Suseong Middle School
2 Yura 17 Yeo Suwon National University
'''






















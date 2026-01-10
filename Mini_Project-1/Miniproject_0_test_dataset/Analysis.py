# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:36:19 2024

@author: Shin
"""

# Combination of genre and other elements (author/product/shortreview) derived using the web_scroll function above

# Import genre dataframe created in MP-Genre-final.py

import pandas as pd 
df_features =pd .read_excel ('./project/book_info.xlsx')
df_genre =pd .read_excel ('./Project/Genrelist_of_bestseller2023.xlsx')
# Merge by column

df_bestseller2023 =pd .concat ([df_features ,df_genre ],axis =1 )

# How many unique genres have been selected for Best Salary in 2023?
genres =df_genre ["장르"].unique ()
print (len (genres ))# 14
# Summary information
df_bestseller2023 .describe ()
'''
Product Author shortreview Genre
count 100 100 100 100
unique 100 99 8 14
top Seino's Teachings David Cho · Hackers Language Institute · 2023.07.24 Helpful novel
freq 1 2 48 22
'''
# You can see that there are a total of 8 types of shortreviews and 14 types of genres.
# It took up the most number of comments with 48 (helpful) one-line comments.
# 22 novels have been confirmed. Let’s check them out for ourselves.
# %%
# Let’s find the proportion of bestseller books by genre.
# Used to count the number of unique values ​​of a series object: value_counts() method
df_bestseller2023 ['장르'].value_counts ()
'''
genre
novel 22
Economy/Management 17
Self-development 15
Humanities 14
foreign language 6
Poetry/Essay 5
Children (elementary school) 5
science 5
cartoon 4
History/Culture 2
Politics/Society 2
health 1
Computer/IT 1
youth 1
Name: count, dtype: int64
'''

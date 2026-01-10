# !/usr/bin/env python
# coding: utf-8

# # Chapter 5 Libraries for data processing and analysis

# ## 5.1 NumPy, efficient for array data operations

# ### 5.1.1 Array data creation

# #### Create an array from list data

# [Chapter 5: Page 146]

# In[ ]:


import numpy as np 

list_data =[0 ,1 ,2 ,3 ,4 ,5.0 ]
a1 =np .array (list_data )
a1 


# [Chapter 5: Page 147]

# In[ ]:


type (a1 )


# In[ ]:


a2 =np .array ([[1 ,2 ,3 ],[4 ,5 ,6 ],[7 ,8 ,9 ]])
a2 


# #### Create an array by specifying the range and spacing

# [Chapter 5: Page 148]

# In[ ]:


np .arange (0 ,10 ,1 )# Specify all start, stop, and step


# In[ ]:


np .arange (0 ,10 )# Specify only start and stop (step=1)


# In[ ]:


np .arange (10 )# Specify only stop (start=0. step=1)


# In[ ]:


np .arange (0 ,5 ,0.5 )# Specify all start, stop, and step


# #### Create an array by specifying the range and number

# [Chapter 5: Page 149]

# In[ ]:


np .linspace (1 ,10 ,10 )# Specify start, stop, num


# In[ ]:


np .linspace (0 ,np .pi ,20 )


# ### 5.1.2 Array data selection

# #### Indexing Arrays

# [Chapter 5: Page 150]

# In[ ]:


import numpy as np 

a1 =np .array ([0 ,10 ,20 ,30 ,40 ,50 ])# Create one-dimensional array
[a1 [0 ],a1 [3 ],a1 [5 ],a1 [-1 ],a1 [-2 ]]# Various examples of array indexing


# In[ ]:


a1 [4 ]=90 
a1 


# In[ ]:


a2 =np .array ([0 ,10 ,20 ,30 ,40 ,50 ])# Create one-dimensional array
a2 [[4 ,0 ,5 ,-1 ,-2 ]]# Select multiple elements by position in array


# [Chapter 5: Page 151]

# In[ ]:


a =np .array ([0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ])
a 


# In[ ]:


a [a >=5 ]


# In[ ]:


a [(a %2 )==0 ]


# In[ ]:


a [((a %2 )==0 )&(a >5 )]# Select only elements that satisfy both conditions simultaneously


# In[ ]:


a [((a %2 )==0 )|(a >5 )]# Select an element even if only one of two conditions is met


# In[ ]:


a [~((a %2 )==0 )]# Select odd numbers using logical negation of the condition for finding even numbers


# #### Slicing an Array

# [Chapter 5: Page 152]

# In[ ]:


import numpy as np 

a1 =np .array ([0 ,10 ,20 ,30 ,40 ,50 ])# Create one-dimensional array

a1 [1 :4 ]# Slicing by specifying both start and end.Selection range: start ~ end-1


# In[ ]:


a1 [:3 ]# Slicing by specifying only the end.Selection range: 0 to end-1


# In[ ]:


a1 [2 :]# Slicing by specifying only start.Selection range: start ~ last_position of array


# In[ ]:


a1 [:]# If neither start nor end are specified, the entire array is selected.


# [Chapter 5: Page 153]

# In[ ]:


a1 [2 :5 ]=np .array ([25 ,35 ,45 ])# Change the element at the selected position (2, 3, 4) to a new array
a1 


# In[ ]:


a1 [3 :6 ]=70 # Change all elements at selected positions (3, 4, 5) to scalar values
a1 


# In[ ]:


a2 =np .array ([0 ,10 ,20 ,30 ,40 ,50 ,60 ,70 ,80 ,90 ])# Create one-dimensional array

a2 [0 :10 :2 ]# 선택 범위: start~end-1, 증가폭(step): 2                             


# In[ ]:


a2 [2 :8 :3 ]# Selection range: start~end-1, increase (step): 3


# In[ ]:


a2 [0 :10 :]# Selection range: start ~ end-1, increase (step): 1


# [Chapter 5: Page 154]

# In[ ]:


a2 [3 ::]# Selection range: start~last position of array, increment (step): 1


# In[ ]:


a2 [:5 :]# Selection range: 0~end-1, increase (step): 1


# In[ ]:


a2 [::]# Selection range: 0 ~ last position of array, increment (step): 1


# In[ ]:


a2 [::-1 ]# Selection range: Last position of array ~ 0, Increment width (step): -1 -> Select in reverse order


# In[ ]:


a2 [8 :2 :-2 ]# Increment amount (step): -2 -> Select in reverse order


# ## 5.2 표 데이터 처리에 강한 판다스(pandas)

# ### 5.1.2 Data structure and creation

# #### Structure and creation of Series data

# [Chapter 5: Page 156]

# In[ ]:


import pandas as pd 

s1 =pd .Series ([10 ,20 ,30 ,40 ,50 ])# Create Series data as a list
s1 


# In[ ]:


s1 .index 


# [Chapter 5: Page 157]

# In[ ]:


s1 .values 


# In[ ]:


import numpy as np 

index_data =['2020-02-27','2020-02-28','2020-02-29','2020-03-01']# specify date
data =[3500 ,3579 ,np .nan ,3782 ]# Data specification

s2 =pd .Series (data ,index =index_data )# Create series data
s2 


# In[ ]:


s3 =pd .Series ({'국어':100 ,'영어':95 ,'수학':90 })
s3 


# [Chapter 5: Page 158]

# In[ ]:


s4 =pd .Series ({'B':4.0 ,'A':5.0 ,'D':2.0 ,'C':3.0 })
s4 


# In[ ]:


s4 .reindex (['A','B','C','D'])


# #### Automatic generation of date data

# [Chapter 5: Page 160]

# In[ ]:


index_data =pd .date_range (start ='2020-02-27',end ='2020-03-01')# Create Date
data =[3500 ,3579 ,np .nan ,3782 ]# Data specification

pd .Series (data ,index =index_data )# Create series data


# In[ ]:


# Create dates from start date to end date every two days (freq='2D')
pd .date_range (start ='2020-07-01',end ='2020-07-10',freq ='2D')


# In[ ]:


# Create dates for a set period (periods=12) based on the start date
pd .date_range (start ='2020-07-01',periods =12 )


# In[ ]:


# Create dates based on business days (freq='B') for the period set based on the start date.
pd .date_range (start ='2020-07-01',periods =12 ,freq ='B')


# [Chapter 5: Page 161]

# In[ ]:


# Create date and time for the period set based on the start date and time (freq='30min')
pd .date_range (start ='2020-07-01 10:00',periods =5 ,freq ='30min')


# #### DataFrame data structure and creation

# [Chapter 5: Page 162]

# In[ ]:


import pandas as pd 

data =[[1 ,2 ,3 ],[4 ,5 ,6 ],[7 ,8 ,9 ]]
df =pd .DataFrame (data )
df 


# [Chapter 5: Page 163]

# In[ ]:


import numpy as np 
import pandas as pd 

data =np .array ([[1 ,2 ,3 ],[4 ,5 ,6 ],[7 ,8 ,9 ],[10 ,11 ,12 ]])# data generation
index_data =pd .date_range ('2023-01-11',periods =4 )# Date data for index
columns_data =['A','B','C']# List data for columns

pd .DataFrame (data ,index =index_data ,columns =columns_data )# Create DataFrame data


# In[ ]:


dict_data ={'연도':[2021 ,2021 ,2022 ,2022 ],
'지사':['한국','미국','한국','미국'],
'고객 수':[200 ,np .nan ,250 ,450 ]}# dictionary data

df =pd .DataFrame (dict_data )# Creating DataFrame data from dictionary data
df 


# [Chapter 5: Page 164]

# In[ ]:


df .index 


# In[ ]:


df .columns 


# In[ ]:


df .values 


# [Chapter 5: Page 165]

# In[ ]:


df1 =df .set_index ("연도")
df1 


# In[ ]:


dict_data ={'A':[10 ,20 ,30 ,40 ,],
'B':[0.1 ,0.2 ,0.3 ,0.4 ],
'C':[100 ,200 ,300 ,400 ]}# dictionary data

df2 =pd .DataFrame (dict_data )# Creating DataFrame data from dictionary data
df2 


# [Chapter 5: Page 166]

# In[ ]:


df2 .reindex ([2 ,0 ,3 ,1 ])


# In[ ]:


df2 .reindex (columns =['B','C','A'])


# ### 5.2.2 Reading and writing tabular data files

# #### Read and write CSV files

# [Chapter 5: Page 168]

# In[ ]:


get_ipython ().run_cell_magic ('writefile','C:/myPyScraping/data/ch05/A_product_sales.csv','연도,1분기,2분기,3분기,4분기\n2016,2412,4032,5183,1139\n2017,2725,4986,6015,1242\n2018,2925,5286,6497,1596\n2019,2691,5813,7202,1358\n2020,2523,6137,7497,1512\n')


# [Chapter 5: Page 169]

# In[ ]:


import pandas as pd 

# CSV file path
folder ='C:/myPyScraping/data/ch05/'# Specify folder
csv_file =folder +'A_product_sales.csv'# Specify file path

# Create DataFrame data by reading CSV file
df =pd .read_csv (csv_file ,encoding ="utf-8")
df 


# In[ ]:


df =pd .read_csv (csv_file ,index_col ="연도")
df 


# [Chapter 5: Page 171]

# In[ ]:


df =pd .DataFrame ({'고객ID':['C5001','C5002','C5003','C5004'],
'국가':['한국','미국','영국','독일'],
'주문금액':[1152000 ,2507000 ,3698000 ,4504100 ]})
df 


# In[ ]:


# CSV file path
folder ='C:/myPyScraping/data/ch05/'# Specify folder
csv_file =folder +'sales_info.csv'# Specify file path

df .to_csv (csv_file )# Write DataFrame data to CSV file
print ("생성한 CSV 파일:",csv_file )# Print the created file name


# [Chapter 5: Page 172]

# In[ ]:


# CSV file path
folder ='C:/myPyScraping/data/ch05/'
csv_file =folder +'sales_info_cp949_encoding.csv'

# Write DataFrame data to CSV file (encoding is 'cp949', does not include index)
df .to_csv (csv_file ,encoding ="cp949",index =False )
print ("생성한 CSV 파일:",csv_file )# Print the created file name


# #### Reading and writing Excel files

# [Chapter 5: Page 174]

# In[ ]:


import pandas as pd 

# Excel file path
folder ='C:/myPyScraping/data/ch05/'
excel_file =folder +'CES마켓_주문내역.xlsx'

# Create DataFrame data by reading an Excel file
df =pd .read_excel (excel_file )
df 


# [Chapter 5: Page 175]

# In[ ]:


df =pd .read_excel (excel_file ,index_col ='주문번호')
# df = pd.read_excel(excel_file, index_col=0) # This method is also possible
df 


# [Chapter 5: Page 177]

# In[ ]:


# Create Pandas DataFrame data
df1 =pd .DataFrame ({'제품ID':['P1001','P1002','P1003','P1004'],
'판매가격':[5000 ,7000 ,8000 ,10000 ],
'판매량':[50 ,93 ,70 ,48 ]})

df2 =pd .DataFrame ({'제품ID':['P2001','P2002','P2003','P2004'],
'판매가격':[5200 ,7200 ,8200 ,10200 ],
'판매량':[51 ,94 ,72 ,58 ]})

df3 =pd .DataFrame ({'제품ID':['P3001','P3002','P3003','P3004'],
'판매가격':[5300 ,7300 ,8300 ,10300 ],
'판매량':[52 ,95 ,74 ,68 ]})

df4 =pd .DataFrame ({'제품ID':['P4001','P4002','P4003','P4004'],
'판매가격':[5400 ,7400 ,8400 ,10400 ],
'판매량':[53 ,96 ,76 ,78 ]})
df1 


# [Chapter 5: Page 178]

# In[ ]:


# Excel file path
folder ='C:/myPyScraping/data/ch05/'
excel_file =folder +'제품_판매현황_1.xlsx'

# Write DataFrame data to Excel file
df1 .to_excel (excel_file )

print ("생성한 엑셀 파일:",excel_file )# Print the created file name


# [Chapter 5: Page 179]

# In[ ]:


# Excel file path
folder ='C:/myPyScraping/data/ch05/'
excel_file =folder +'제품_판매현황_2.xlsx'

# Write DataFrame data to Excel (specify option)
df1 .to_excel (excel_file ,sheet_name ='제품_라인업1',index =False )

print ("생성한 엑셀 파일:",excel_file )# Print the created file name


# In[ ]:


# Excel file path
folder ='C:/myPyScraping/data/ch05/'
excel_file =folder +'제품_판매현황_two_sheets.xlsx'

# Write DataFrame data to ‘Product_Lineup1’ and ‘Product_Lineup2’ sheets in Excel file.
with pd .ExcelWriter (excel_file ,engine ='xlsxwriter')as excel_writer :
    df1 .to_excel (excel_writer ,sheet_name ='제품_라인업1',index =False )
    df2 .to_excel (excel_writer ,sheet_name ='제품_라인업2',index =False )

print ("생성한 엑셀 파일:",excel_file )# Print the created file name


# [Chapter 5: Page 180]

# In[ ]:


# Excel file path to print
folder ='C:/myPyScraping/data/ch05/'
excel_file =folder +'제품_판매현황_전체_one_worksheet.xlsx'

# 1) Write DataFrame data (df) using the created object (excel_writer)
excel_writer =pd .ExcelWriter (excel_file ,engine ='xlsxwriter')

# 2) Output multiple DataFrame data in different locations on one Excel worksheet
df1 .to_excel (excel_writer )# Same as startrow=0, startcol=0
df2 .to_excel (excel_writer ,startrow =0 ,startcol =5 ,index =False )
df3 .to_excel (excel_writer ,startrow =6 ,startcol =0 )
df4 .to_excel (excel_writer ,startrow =6 ,startcol =5 ,index =False ,header =False )

# 3) Close the object and save it as an Excel file
excel_writer .save ()

print ("생성한 엑셀 파일:",excel_file )# Print the created file name


# ### 5.2.3 Select table data

# #### Select row data

# [Chapter 5: Page 183]

# In[ ]:


import pandas as pd 
import numpy as np 

index_data =['a','b','c','d','e']# Data for index
data =[0.0 ,1.0 ,2.0 ,3.0 ,4.0 ]# data
s1 =pd .Series (data ,index =index_data )
s1 


# In[ ]:


s1 .loc ['a']# Select one row data by specifying index label


# In[ ]:


s1 .loc [['a','c','e']]# Select data from multiple rows by specifying a list of index labels


# In[ ]:


s1 .loc [['e','b','a']]# Select data from multiple rows by specifying a list of index labels


# [Chapter 5: Page 184]

# In[ ]:


s1 .loc ['b':'d']# Select data from multiple rows with index label slicing


# In[ ]:


s1 .iloc [1 ]# Select one row of data by specifying the index position


# In[ ]:


s1 .iloc [[0 ,2 ,4 ]]# Select data from multiple rows by specifying a list of index positions


# In[ ]:


s1 .iloc [1 :4 ]# Select data from multiple rows by index position slicing


# In[ ]:


s1 .loc ['a':'c']=10 # Assigning scalar values ​​to multiple rows of data
s1 


# [Chapter 5: Page 185]

# In[ ]:


s1 .iloc [3 :5 ]=20 
s1 


# In[ ]:


dict_data ={'A':[0 ,10 ,20 ,30 ,40 ],
'B':[0 ,0.1 ,0.2 ,0.3 ,0.4 ],
'C':[0 ,100 ,200 ,300 ,400 ]}# dictionary data

index_data =['a','b','c','d','e']# Data for index designation

df1 =pd .DataFrame (dict_data ,index =index_data )# Creating DataFrame data from dictionary data
df1 


# In[ ]:


df1 .loc ['a']# Select one row of data by specifying index label


# [Chapter 5: Page 186]

# In[ ]:


df1 .loc [['a','c','e']]# Select data from multiple rows by specifying a list of index labels


# In[ ]:


df1 .loc ['b':'d']# Select data from multiple rows with index label slicing


# In[ ]:


df1 .iloc [2 ]# Select one row of data by specifying the index position


# In[ ]:


df1 .iloc [[1 ,3 ,4 ]]# Select data from multiple rows by specifying a list of index positions


# [Chapter 5: Page 187]

# In[ ]:


df1 .iloc [1 :3 ]# Select data from multiple rows by index position slicing


# In[ ]:


df1 .loc ['a':'c']=50 
df1 


# [Chapter 5: Page 188]

# In[ ]:


# Create series data
s =pd .Series (range (-3 ,6 ))
s 


# In[ ]:


# Create DataFrame data
dict_data ={'지점':['서울','대전','대구','부산','광주'],
'1월':[558 ,234 ,340 ,380 ,213 ],
'2월':[437 ,216 ,238 ,290 ,194 ],
'3월':[337 ,196 ,209 ,272 ,186 ]}# dictionary data

df =pd .DataFrame (dict_data )# Creating DataFrame data from dictionary data
df 


# In[ ]:


s [s >0 ]# Get row data that satisfies conditions


# [Chapter 5: Page 189]

# In[ ]:


s [(s >=-2 )&(s %2 ==0 )]# Get row data that satisfies both conditions


# In[ ]:


df [df ['1월']>=300 ]# Get row data that satisfies conditions


# In[ ]:


df [(df ['지점']=='서울')|(df ['지점']=='부산')]# Select a row even if only one of the two is satisfied


# [Chapter 5: Page 190]

# In[ ]:


df [df ['지점'].isin (['서울','부산'])]


# In[ ]:


dict_data ={'제품ID':['P501','P502','P503','P504','P505','P506','P507'],
'판매가격':[6400 ,5400 ,9400 ,10400 ,9800 ,1200 ,3400 ],
'판매량':[63 ,56 ,98 ,48 ,72 ,59 ,43 ],
'이익률':[0.30 ,0.21 ,0.15 ,0.25 ,0.45 ,0.47 ,0.32 ]}# dictionary data

df2 =pd .DataFrame (dict_data )
df2 


# [Chapter 5: Page 191]

# In[ ]:


df2 .head ()# Select first 5 rows of data


# In[ ]:


df2 .head (2 )# Select first 2 rows of data


# [Chapter 5: Page 192]

# In[ ]:


df2 .tail ()# Select last 5 rows of data


# In[ ]:


df2 .tail (3 )# Select last 3 rows of data


# In[ ]:


with pd .option_context ('display.max_rows',4 ):
    pd .set_option ("show_dimensions",False )
    display (df2 )


    # #### Select column data

    # [Chapter 5: Page 193]

    # In[ ]:


df2 ['제품ID']


# [Chapter 5: Page 194]

# In[ ]:


df2 [['제품ID']]


# In[ ]:


df2 [['제품ID','이익률','판매가격']]


# [Chapter 5: Page 195]

# In[ ]:


# Change all values ​​in specified column data to scalar values
df2 ['이익률']=0.5 # Change 'Profit Margin' column data to 0.5
df2 


# #### Select row and column data

# In[ ]:


dict_data ={'A':[0 ,1 ,2 ,3 ,4 ],
'B':[10 ,11 ,12 ,13 ,14 ],
'C':[20 ,21 ,22 ,23 ,24 ]}# dictionary data

index_data =['a','b','c','d','e']# Data for index designation

df =pd .DataFrame (dict_data ,index =index_data )# Create DataFrame data
df 


# [Chapter 5: Page 196]

# In[ ]:


df .loc ['a','A']# use loc


# In[ ]:


df .iloc [0 ,0 ]# Use iloc


# In[ ]:


df .loc ['a':'c',['A','B']]# use loc


# In[ ]:


df .iloc [0 :3 ,0 :2 ]# Use iloc


# [Chapter 5: Page 197]

# In[ ]:


df .loc [:,['A','B']]# use loc


# In[ ]:


df .iloc [:,0 :2 ]# Use iloc


# In[ ]:


df .loc [df ['A']>2 ,['A','B']]# use loc


# [Chapter 5: Page 198]

# In[ ]:


df .loc ['a':'c',['A','B']]=50 # Specify scalar value
df 


# In[ ]:


df .iloc [3 :5 ,1 :3 ]=100 # Specify scalar value
df 


# In[ ]:


df .loc [df ['B']<70 ,'B']=70 # Specify scalar value
df 


# [Chapter 5: Page 199]

# In[ ]:


df .loc [df ['C']<30 ,'D']=40 # Use loc.Specify scalar value
df 


# ### 5.2.4 Table data integration

# [Chapter 5: 200 pages]

# In[ ]:


import pandas as pd 

s1 =pd .Series ([10 ,20 ,30 ])
s1 


# In[ ]:


s2 =pd .Series ([40 ,50 ,60 ])
s2 


# In[ ]:


s3 =pd .Series ([70 ,80 ,90 ])
s3 


# In[ ]:


# Connect vertically
pd .concat ([s1 ,s2 ])


# [Chapter 5: Page 201]

# In[ ]:


# Ignore the existing index and create a new index
pd .concat ([s1 ,s2 ],ignore_index =True )


# In[ ]:


# Ignore the existing index and create a new index
pd .concat ([s1 ,s2 ,s3 ],ignore_index =True )


# [Chapter 5: Page 202]

# In[ ]:


df1 =pd .DataFrame ({'물리':[95 ,92 ,98 ,100 ],
'화학':[91 ,93 ,97 ,99 ]})
df1 


# In[ ]:


df2 =pd .DataFrame ({'물리':[87 ,89 ],
'화학':[85 ,90 ]})
df2 


# In[ ]:


df3 =pd .DataFrame ({'물리':[72 ,85 ]})
df3 


# In[ ]:


df4 =pd .DataFrame ({'생명과학':[94 ,91 ,94 ,83 ],
'지구과학':[86 ,94 ,89 ,93 ]})
df4 


# [Chapter 5: Page 203]

# In[ ]:


# Connect vertically (ignore existing index)
pd .concat ([df1 ,df2 ],ignore_index =True )


# In[ ]:


# Connect vertically (ignore existing index)
pd .concat ([df2 ,df3 ],ignore_index =True )


# [Chapter 5: Page 204]

# In[ ]:


# Connect only common data vertically (ignoring existing indexes)
pd .concat ([df2 ,df3 ],ignore_index =True ,join ='inner')


# In[ ]:


# Connect horizontally
pd .concat ([df1 ,df4 ],axis =1 )


# In[ ]:


# Connect all data in landscape orientation
pd .concat ([df2 ,df4 ],axis =1 )


# [Chapter 5: Page 205]

# In[ ]:


# Connect only common data horizontally
pd .concat ([df2 ,df4 ],axis =1 ,join ='inner')


# ## 5.3 Summary

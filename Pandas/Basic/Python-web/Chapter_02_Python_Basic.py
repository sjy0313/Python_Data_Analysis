# !/usr/bin/env python
# coding: utf-8

# # Chapter 2 Python Basic Grammar

# ## 2.1 Variables and data types

# ### 2.1.1 Variables

# [Chapter 2: Page 33]

# In[1]:


abc =12340 # Assign the number 12340 to the abc variable
print (abc +100 )# Add 100 to the abc variable and print the result


# In[2]:


string1 ="Python is "
string2 ="powerful."
print (string1 +string2 )


# ### 2.1.2 Number (int, float)

# [Chapter 2: Page 35]

# In[ ]:


type (123 )


# In[ ]:


type (123.45 )


# In[ ]:


5 +2 


# [Chapter 2: Page 36]

# In[ ]:


print (5 +2 )# plus
print (5 -2 )# subtraction
print (5 *2 )# multiply
print (5 /2 )# divide
print (5 //2 )# Find the quotient
print (5 %2 )# Find the remainder
print (5 **2 )# power


# [Chapter 2: Page 37]

# In[ ]:


6 /3 


# In[ ]:


(10 /5 +(5 -2 ))*(1.2 +2 )/2 **2 


# ### 2.1.3 String (str)

# [Chapter 2: Page 37]

# In[ ]:


"String"


# In[ ]:


'Test'


# [Chapter 2: Page 38]

# In[ ]:


print ("String")
print ('Test')


# In[ ]:


print ("It's OK.")


# In[ ]:


print ('그는 "파이썬이 무엇입니까?"라고 물었습니다.')


# In[ ]:


type ('Hello Python!')


# In[ ]:


"Hello"+" "+"Python "+"!"


# In[ ]:


"Python"*3 


# [Chapter 2: Page 39]

# In[ ]:


len ("Python")


# In[ ]:


len ("Python ")


# In[ ]:


long_str ='''學而不思則罔 思而不學則殆
학이불사즉망 사이불학즉태
"배우기만 하고 생각하지 않으면 얻는 것이 없고, 생각만 하고 배우지 않으면 위태롭다."
(출처: 『논어』위정편 15장)'''

print (long_str )


# ### 2.1.4 bool

# [Chapter 2: Page 40]

# In[ ]:


print (True )


# In[ ]:


print (False )


# In[ ]:


type (True )


# In[ ]:


type (False )


# [Chapter 2: Page 41]

# In[ ]:


print (True and False )
print (True or False )
print (not False )


# In[ ]:


# Examples of using comparison operators for numeric data types
print (10 ==5 )# 10 and 5 are the same --> False
print (10 !=5 )# 10 and 5 are not equal --> True
print (10 <5 )# 10 is less than 5 --> False
print (10 >5 )# 10 is greater than 5 --> True
print (10 <=5 )# 10 is less than or equal to 5 --> False
print (10 >=5 )# 10 is greater than or equal to 5 --> True

# Examples of using comparison operators for Boolean data types
print (True ==False )# True and False are the same --> False
print (True !=False )# True and False are not the same --> True


# [Chapter 2: Page 42]

# In[ ]:


1 >0 and (5 >10 or 3 <5 )


# ### 2.1.5 List

# #### Create a list

# [Chapter 2: Page 43]

# In[ ]:


list_num =[10 ,20 ,30 ,40 ]# Organize lists with numbers
list_str =['programming','language','python']# Constructing a list with strings
list_mix1 =[1.5 ,2.6 ,'문자열1','문자열2']# Construct a list with numbers and strings
list_mix2 =[4.0 ,True ,'abc',list_mix1 ]# Compose a list with numbers, numbers, strings, and lists.
list_empty =[]# empty list with no elements

print (list_num )
print (list_str )
print (list_mix1 )
print (list_mix2 )
print (list_empty )


# [2장: 44페이지]

# In[ ]:


type (list_empty )


# In[ ]:


print (len (list_num ))# Number of elements: 4
print (len (list_str ))# Number of elements: 3
print (len (list_mix1 ))# Number of elements: 4
print (len (list_mix2 ))# Number of elements: 4
print (len (list_empty ))# Number of elements: 0


# #### list operators

# [Chapter 2: Page 44]

# In[ ]:


list_str1 =["기술이 ","강한 나라 "]
list_str2 =["우리나라 ","대한민국 "]
list_str3 =list_str1 +list_str2 # Create a new list by concatenating the elements of two lists.
list_str4 =list_str2 *2 # Create a new list by repeatedly connecting the elements of the list

print (list_str3 )
print (list_str4 )


# #### List indexing

# [Chapter 2: Page 45]

# In[ ]:


print (list_num )# list_num output
print (list_num [0 ])# Get the first element of list_num
print (list_num [1 ])# Get the second element of list_num
print (list_num [2 ])# Get the third element of list_num
print (list_num [3 ])# Get the fourth element of list_num


# [Chapter 2: Page 46]

# In[ ]:


print (list_num [-1 ])# Get the last element of list_num
print (list_num [-2 ])# Get the element before the last element of list_num


# In[ ]:


print (list_mix2 )# list_mix2 output
print (list_mix2 [3 ])# Get fourth element from list_mix2
print (list_mix2 [3 ][2 ])# Gets the third element from the list, which is the fourth element


# In[ ]:


list_num1 =[100 ,200 ,300 ,400 ]# Create list
print (list_num1 )

list_num1 [1 ]=500 # Assign new data to the second element
print (list_num1 )


# [Chapter 2: Page 47]

# In[ ]:


list_num2 =[0 ,10 ,20 ,30 ,40 ,50 ]# Organize lists with numbers
print (list_num2 )

del list_num2 [2 ]# Remove element with index 2 from list
print (list_num2 )


# #### List slicing

# [Chapter 2: Page 48]

# In[ ]:


list_num3 =[0 ,10 ,20 ,30 ,40 ,50 ,60 ,70 ,80 ,90 ]# Create list

print (list_num3 )# list output
print (list_num3 [0 :4 ])# Index range: 0 to 3
print (list_num3 [5 :10 ])# Index range: 5 to 9


# In[ ]:


print (list_num3 [:4 ])# Omit start.Index range: 0 to 3
print (list_num3 [5 :])# Omit end.Index range: 5 to end (9)
print (list_num3 [:])# Both start and end are omitted.Index range: All indices


# #### Check for existence of list element

# [Chapter 2: Page 49]

# In[ ]:


list_num6 =[0 ,1 ,2 ,3 ]# Create list

print (2 in list_num6 )# 2 is in list: returns True
print (5 in list_num6 )# 5 is not in the list: returns False


# #### list methods

# [Chapter 2: Page 50]

# In[ ]:


friends =['토마스']# create a list
print (friends )

friends .append ('고든')# Add an element ('Gordon') to the end of the list
print (friends )

friends .append ('에드워드')# Add an element ('Edward') to the end of the list
print (friends )


# ### 2.1.6 tuple

# #### Create a tuple

# [Chapter 2: Page 51]

# In[ ]:


tuple_num1 =(0 ,1 ,2 ,3 ,4 )# Creating tuples with parentheses
tuple_num2 =5 ,6 ,7 ,8 ,9 # Create a tuple without parentheses

print (tuple_num1 )
print (tuple_num2 )


# In[ ]:


type (tuple_num1 )


# In[ ]:


type (tuple_num2 )


# [Chapter 2: Page 52]

# In[ ]:


tuple_num3 =(10 ,)# Creating a tuple with one element using parentheses
tuple_num4 ="데이터1",# Create a tuple with one element without parentheses

print (tuple_num3 )
print (tuple_num4 )


# #### Handling tuples

# [Chapter 2: Page 52]

# In[ ]:


tuple_mixed1 =('programming','language','python',1 ,2 ,3 )# Create tuple
print (tuple_mixed1 [0 ])# Tuple indexing
print (tuple_mixed1 [0 :4 ])# Tuple slicing (select elements from index 0 to 3)


# In[ ]:


tuple_mixed1 [3 ]=10 # An error occurs because the elements of the tuple cannot be changed.


# ### 2.1.7 set

# #### Create a set

# [Chapter 2: Page 53]

# In[ ]:


set_num ={10 ,100 ,2 ,3 ,4 ,4 ,5 }
set_str ={"사과","배","오렌지","귤","귤"}

print (set_num )
print (set_str )


# [2장: 54페이지]

# In[ ]:


type (set_str )


# In[ ]:


set_num [0 ]


# #### Intersection, union, difference of sets

# [Chapter 2: Page 54]

# In[ ]:


set_A ={0 ,1 ,2 ,3 ,4 }# set (set) A
set_B ={3 ,4 ,5 ,6 ,7 }# set (collection) B

# Using &, |, - operators
print (set_A &set_B )# Intersection of sets A and B (A∩B)
print (set_A |set_B )# Union of sets A and B (A∪B)
print (set_A -set_B )# Difference of sets A and B (A—B)

# Using intersection(), union(), difference() methods
print (set_A .intersection (set_B ))# Intersection of sets A and B (A∩B)
print (set_A .union (set_B ))# Union of sets A and B (A∪B)
print (set_A .difference (set_B ))# Difference of sets A and B (A—B)


# ### 2.1.8 Dictionary (dict)

# #### Creating a dictionary

# [Chapter 2: Page 55]

# In[ ]:


dict_ex1 ={1 :'사과',2 :'배',3 :'복숭아',4 :'딸기'}# Keys are numbers, values ​​are strings
dict_ex2 ={1 :1234 ,5 :5678 ,7 :7890 }# Both keys and values ​​are numbers
dict_ex3 ={True :'맞습니다.',False :'아닙니다.'}# Key is boolean, value is string
dict_ex4 ={'ID_101':['민준',24 ],'ID_102':['서연',27 ]}# Keys are strings, values ​​are lists

print (dict_ex1 )
print (dict_ex2 )
print (dict_ex3 )
print (dict_ex4 )


# [Chapter 2: Page 56]

# In[ ]:


type (dict_ex4 )


# In[ ]:


dict_ex5 =dict (a =10 ,b =2.0 ,c ='string',d =True ,abc =[1 ,2 ,3 ])
dict_ex5 


# #### Selecting, changing, adding, and deleting values ​​using dictionary keys

# [Chapter 2: Page 57]

# In[ ]:


print (dict_ex1 [1 ])
print (dict_ex2 [7 ])
print (dict_ex3 [True ])
print (dict_ex4 ['ID_102'])
print (dict_ex5 ['b'])


# In[ ]:


dict_user ={"이름":"박재민","나이":24 }# Create dictionary
print (dict_user )

dict_user ["나이"]=25 # Change value to existing key
print (dict_user )

dict_user ["취미"]=["게임","농구"]# Add a new key and value pair
print (dict_user )


# [Chapter 2: Page 58]

# In[ ]:


dict_user2 ={'이름':'조수빈','나이':28 ,'취미':['독서','영화']}
print (dict_user2 )

del dict_user2 ['취미']# Delete a specific key/value pair from a dictionary using del.
print (dict_user2 )


# #### Check for existence of dictionary key

# [Chapter 2: Page 58]

# In[ ]:


dict_vehicle ={'버스':1 ,'기차':2 ,'배':3 ,'비행기':4 }# Create dictionary

print ('기차'in dict_vehicle )# dict_vehicle has 'train' in its key
print ('택시'in dict_vehicle )# There is no 'taxi' in the key of dict_vehicle


# #### Dictionary methods

# [Chapter 2: Page 59]

# In[ ]:


dict_num_alpha ={0 :'a',1 :'b',2 :'c',3 :'d',4 :'e'}# Create dictionary
print (dict_num_alpha )# output dict_num_alpha
print (dict_num_alpha .keys ())# Get the keys of a dictionary
print (dict_num_alpha .values ())# Get the value of a dictionary
print (dict_num_alpha .items ())# Retrieve key and value pairs from a dictionary


# [Chapter 2: Page 60]

# In[ ]:


print (list (dict_num_alpha .keys ()))# Convert the return result of the dictionary key to a list
print (list (dict_num_alpha .values ()))# Convert the return result of dictionary values ​​to a list
print (list (dict_num_alpha .items ()))# Returns dictionary key and value pairs and converts the result to a list


# In[ ]:


print (dict_num_alpha )# Existing dictionary output

dict_new ={5 :'f',6 :'g'}# Create dictionary
dict_num_alpha .update (dict_new )# Add key and value pairs from a new dictionary to an existing dictionary.
print (dict_num_alpha )# Print dictionary after adding a new dictionary


# In[ ]:


print (dict_num_alpha .get (1 ))# If the input value is in a dictionary key, the corresponding value is returned.
print (dict_num_alpha .get (7 ))# Returns None if the input value is not in the dictionary key.


# [Chapter 2: Page 61]

# In[ ]:


dict_num_eng ={0 :'zero',1 :'one',2 :'two',3 :'three'}
print (dict_num_eng )

dict_num_eng .clear ()# Delete all key and value pairs from dictionary
print (dict_num_eng )


# ## 2.2 Control statements

# ### 2.2.1 Conditional statements

# #### Branching based on a single condition: if

# [Chapter 2: Page 62]

# In[ ]:


x =95 # Assign 95 to x

if x >=90 :# <Conditions>
    print ("합격")# If <condition> is true, execute <code block>


    # #### Branching based on a single condition and more: if ~ else

    # [Chapter 2: Page 63]

    # In[ ]:


x =85 # x에 85를 할당

if x >=90 :# <Conditions>
    print ("축하합니다.")# <Code block 1>
    print ("당신은 합격입니다.")# If <condition> is true, perform <code block 1>
else :
    print ("죄송합니다.")# <Code block 2>
    print ("당신은 불합격입니다.")# If <condition> is not true, perform <code block 2>


    # #### 여러 조건에 따른 분기: if ~ elif ~ else

    # [Chapter 2: Page 64]

    # In[ ]:


x =75 # Assign 75 to x

if x >=90 :# <Condition 1>
    print ("학점: A")# <Code block 1>
elif 80 <=x <90 :# <Condition 2>: 80 <= x < 90 is equivalent to (x >= 80) and (x < 90)
    print ("학점: B")# <Code block 2>
elif 70 <=x <80 :# <Condition 3>
    print ("학점: C")# <Code block 3>
else :
    print ("학점: D")# <Code block 4>


    # In[ ]:


x =100 

if x >=90 :
    if x ==100 :
        print ("만점으로 합격")
    else :
        print ("합격")
else :
    print ("불합격")


    # ### 2.2.2 Loop

    # #### for loop

    # [Chapter 2: Page 65]

    # In[ ]:


for num in [0 ,1 ,2 ,3 ,4 ,5 ]:
    print (num )


    # [Chapter 2: Page 66]

    # In[ ]:


list (range (0 ,10 ,1 ))


# In[ ]:


list (range (10 ))


# In[ ]:


for num in range (6 ):
    print (num )


    # [Chapter 2: Page 67]

    # In[ ]:


list_num =[10 ,20 ,30 ,40 ]

for index ,value in enumerate (list_num ):
     print (index ,value )


     # In[ ]:


names =["남온조","이청산","최남라","이수혁","이나연","양대수"]# name
scores =[96 ,85 ,100 ,70 ,80 ,75 ]# test score


# In[ ]:


for k in range (len (names )):
    print (names [k ],scores [k ])


    # [Chapter 2: Page 68]

    # In[ ]:


for name ,score in zip (names ,scores ):
    print (name ,score )


    # #### while loop

    # [Chapter 2: Page 69]

    # In[ ]:


list_num =[]# Create an empty list
count =0 # Initialize count to 0

while (count <10 ):# <Condition> Check if count is less than 10
    list_num .append (count )# <code block> Add count to list_num
    count =count +1 # <code block> Increment count by 1

print (list_num )# Print the contents of list list_num


# #### break and continue change the flow of repetition

# [Chapter 2: Page 69]

# In[ ]:


num =[1 ,2 ,3 ,4 ,5 ,6 ]
num_sum =0 # Initialize the sum of numbers to 0
count =0 # Initialize count to 0

while True :
    num_sum =num_sum +num [count ]# Add elements of list num one by one
    print (num_sum )
    if (num_sum >=10 ):# Check if sum (num_sum) is greater than 10
        print ("while 문을 끝냅니다.")
        break # End while statement

    count =count +1 # Increase count by 1


    # [Chapter 2: Page 70]

    # In[ ]:


months =[1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ]
months_data =[15 ,21 ,33 ,17 ,19 ,22 ,16 ,25 ,27 ,18 ,13 ,14 ]
data_sum =0 # Reset the numeric sum

for month ,data in zip (months ,months_data ):
    if (month ==5 ):
        print ('해당 월의 데이터를 제외합니다.')
        continue # Proceed to the next iteration without executing any further code.
    data_sum =data_sum +data # Find the sum of monthly data

print (data_sum )# Print the total calculated in the for statement


# #### One-line for loop

# [Chapter 2: Page 71]

# In[ ]:


numbers =[0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ]# Create list

# Create a new list by performing 2*x+1 operation on each element of the list.
result =[2 *x +1 for x in numbers ]

print (result )# Print the generated list


# In[ ]:


numbers =[0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ]# Create list

# 2*x+1 operation is performed only when the condition x >=3 is satisfied.
result =[2 *x +1 for x in numbers if x >=3 ]

print (result )# Print the generated list


# ## 2.3 Data output

# ### 2.3.1 Basic output

# [Chapter 2: Page 72]

# In[ ]:


print (1 ,2 ,3 ,4 ,5 )# numeric output
print ('a','b','c','d','e')# character output
print (123 ,"abc",True )# Number, letter, fire output
print (['abc',123 ,'def'],{"a":1 ,"b":2 })# List and dictionary output


# [Chapter 2: Page 73]

# In[ ]:


print ("합계:")# If there is no end option, a newline character is inserted to perform a line break.
print (90 )
print ("합계:",end ='')# Enter an empty string in the end option to prevent line breaks.
print (90 )


# In[ ]:


print ("나는 파이썬을 이용해 \n많은 업무를 \n자동화합니다.")


# ### 2.3.2 Formatted output

# [Chapter 2: Page 73]

# In[ ]:


fruit_0 ="Banana"
fruit_1 ="Apple"
fruit_2 ="Orange"

print ("문자열 출력: {0}, {1}, {2}".format (fruit_0 ,fruit_1 ,fruit_2 ))
print ("문자열 출력: {2}, {0}, {1}".format (fruit_0 ,fruit_1 ,fruit_2 ))


# [Chapter 2: Page 74]

# In[ ]:


print ("문자열 출력: {}, {}, {}".format (fruit_0 ,fruit_1 ,fruit_2 ))


# In[ ]:


num_int =123 
num_float =3.14159265358979323846 

print ("숫자 출력: {0}, {1}".format (num_int ,num_float ))


# [Chapter 2: Page 75]

# In[ ]:


list_num_ints =[1 ,12 ,123 ,1234 ,12345 ]# Create list

print ("[숫자(정수)의 출력 형식을 지정하지 않고 출력]")
for list_num_int in list_num_ints :
    print ("{0}".format (list_num_int ))# Output format not specified

print ("\n[숫자(정수)의 출력 형식을 지정해 출력]")
for list_num_int in list_num_ints :
    print ("{0:6d}".format (list_num_int ))# Specify output format (number of output digits of integer)


    # In[ ]:


print ("[숫자(실수)의 출력 형식을 지정해 출력]")
print ("{0:.2f}, {0:.5f}, {0:.0f}".format (num_float ))


# [Chapter 2: Page 76]

# In[ ]:


temp_c =10.5 # degrees celsius
temp_f =(temp_c *9 /5 )+32 # Convert to Fahrenheit temperature conversion

# Assign the result of string.format() to a variable
format_str ="변환 결과: 섭씨 {0:.1f}도 → 화씨 {1:.1f}도".format (temp_c ,temp_f )

print (format_str )# Print the contents of the variable


# In[ ]:


user_name ="홍길동"
user_number ="1234-5678"

print ("고객 이름:{name}, 고객 번호:{number}".format (name =user_name ,number =user_number ))


# [Chapter 2: Page 77]

# In[ ]:


name ="최서희"
phone_number ="010-xyz-1234"

print (f"이름: {name }, 전화번호: {phone_number }")# Output using f-string method


# In[ ]:


r =2 # radius
pi =3.141592 # pie

print (f"제품 가격: {57250000 :,}원")# Enter the value directly in {Expression}
print (f"파이(소수점 6자리까지): {pi :.6f}")# Enter variable in {Expression content}
print (F"반지름이 {r }인 원의 넓이: {pi *r **2 :.2f}")# Enter the calculation formula in {Expression Content}


# ## 2.4 Exception handling

# ### 2.4.1 Using try ~ except

# [Chapter 2: Page 78]

# In[ ]:


10 /0 


# [Chapter 2: Page 79]

# In[ ]:


try :
    10 /0 
except :
    print ("실행 중 오류가 발생했습니다.")


    # In[ ]:


try :
    10 /0 
except ZeroDivisionError :
    print ("실행 중 숫자를 0으로 나누었습니다.")


    # In[ ]:


try :
    for k in [1 ,2 ,3 ]:
        if (k ==3 ):
            print ("k = {0}. 일부러 오류 발생".format (k ))
            raise 
        else :
            print ("k = {0}".format (k ))
except :
    print ("실행 중 오류가 발생했습니다.")


    # ### 2.4.2 Using try ~ finally

    # [Chapter 2: Page 80]

    # In[ ]:


tuple_num =(1 ,2 ,3 )# tuple data

try :
    tuple_num [0 ]=4 # Error occurs because elements of tuple cannot be changed
except :
    print ("오류가 발생했습니다.")
finally :
    print ("tuple_num = {0}".format (tuple_num ))


    # ## 2.5 Summary

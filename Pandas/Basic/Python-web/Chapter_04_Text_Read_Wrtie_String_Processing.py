# !/usr/bin/env python
# coding: utf-8

# # Chapter 4 Reading and writing files and string processing

# ## 4.1 Reading and writing files

# ### 4.1.1 Basic structure for reading and writing files

# ### 4.1.2 Reading files

# [Chapter 4: Page 130]

# In[ ]:


get_ipython ().run_cell_magic ('writefile','C:\\myPyScraping\\data\\ch04\\read_test.txt','All grown-up\nwere once children,\nalthough few of them\nremember it.\n')


# [Chapter 4: Page 131]

# In[ ]:


f =open ('C:/myPyScraping/data/ch04/read_test.txt','r')# Open file (read mode)
data =f .read ()# Read the entire contents of the file and assign it to a variable
f .close ()# Close file

print (data )# Print the contents of the read file


# In[ ]:


# Reading Korean text files encoded with cp949
file_name ='C:/myPyScraping/data/ch04/헌법_cp949.txt'# Assign file path to variable

f =open (file_name ,'r',encoding ='cp949')# Open file (read mode)
# f = open(file_name)
data =f .read ()# Read the entire contents of the file and assign it to a variable
f .close ()# Close file

print (data )# Print the contents of the read file


# [Chapter 4: Page 132]

# In[ ]:


# Reading Korean text files encoded in UTF-8
file_name ='C:/myPyScraping/data/ch04/헌법_utf8.txt'# Assign file path to variable

f =open (file_name ,'r',encoding ='utf-8')# Open file (read mode)
data =f .read ()# Read the entire contents of the file and assign it to a variable
f .close ()# Close file

print (data )# Print the contents of the read file


# ### 4.1.3 Reading and processing a file line by line

# #### Read line by line: `readline()`

# [Chapter 4: Page 133]

# In[ ]:


file_name ='C:/myPyScraping/data/ch04/read_test.txt'# Assign file path to variable

f =open (file_name ,'r')# Open file (read mode)

line1 =f .readline ()# Read the contents of the file line by line and assign it to a variable
line2 =f .readline ()# Read the contents of the file line by line and assign it to a variable
f .close ()# Close file

print (line1 ,end ='')# Prints the content without printing the newline character of print itself.
print (line2 ,end ='')


# In[ ]:


file_name ='C:/myPyScraping/data/ch04/read_test.txt'# Assign file path to variable

f =open (file_name ,'r')# Open file (read mode)
line_num =0 # Initializing variable to display number of lines

while True :
    line =f .readline ()# Read the contents of the file line by line and assign it to a variable
    if (line ==''):# Check if line is an empty string
        break # If the string is empty, exit the while statement.
    line_num =line_num +1 # Increase line_num by 1
    print ("{0}: {1}".format (line_num ,line ),end ='')# Number of lines and output string read

f .close ()# Close file


# #### Reading a list with each line as an element: `readlines()`

# [Chapter 4: Page 134]

# In[ ]:


file_name ='C:/myPyScraping/data/ch04/read_test.txt'# Assign file path to variable

f =open (file_name ,'r')# Open file (read mode)
lines =f .readlines ()# Read the contents of the entire file and assign it to a variable
f .close ()# Close file

print (lines )


# In[ ]:


file_name ='C:/myPyScraping/data/ch04/read_test.txt'# Assign file path to variable

f =open (file_name ,'r')# Open file (read mode)
lines =f .readlines ()# Read the contents of the entire file and assign it to a variable
f .close ()# Close file

line_num =0 # Initializing variable to display number of lines
for line in lines :
    line_num =line_num +1 # Increase line_num by 1
    print ("{0}: {1}".format (line_num ,line ),end ='')# Number of lines and output string read


    # ### 4.1.4 Writing files

    # [Chapter 4: Page 135]

    # In[ ]:


file_name ='C:/myPyScraping/data/ch04/write_test.txt'# Assign file path to variable

f =open (file_name ,'w')# Open file (write mode)
f .write ("Python is powerful... and fast;\n")# write string to file
f .write ("plays well with others;\n")
f .write ("runs everywhere;\n")
f .write ("is friendly & easy to learn;\n")
f .write ("is Open.\n")
f .close ()# Close file

print ("생성한 파일:",file_name )# Print the created file name


# [Chapter 4: Page 136]

# In[ ]:


get_ipython ().system ('type C:\\myPyScraping\\data\\ch04\\write_test.txt')


# In[ ]:


file_name ='C:/myPyScraping/data/ch04/two_times.txt'# Assign file path to variable

f =open (file_name ,'w')# Open file (write mode)
f .write ("[구구단 2단의 일부]\n")
for num in range (1 ,6 ):# for statement: num repeats from 1 to 5
    format_string ="2 x {0} = {1}\n".format (num ,2 *num )# Create a string to save
    f .write (format_string )# write string to file
f .close ()# Close file

print ("생성한 파일:",file_name )# Print the created file name


# In[ ]:


get_ipython ().system ('type C:\\myPyScraping\\data\\ch04\\two_times.txt')


# ### 4.1.5 Reading and writing files with the with statement

# [Chapter 4: Page 137]

# In[ ]:


file_name ='C:/myPyScraping/data/ch04/three_times.txt'# Assign file path to variable

with open (file_name ,'w')as f :# Open file (write mode)
    f .write ("[구구단 3단의 일부]\n")
    for num in range (1 ,6 ):# for statement: num repeats from 1 to 5
        format_string ="3 x {0} = {1}\n".format (num ,3 *num )# Create a string to save
        f .write (format_string )# write string to file


        # In[ ]:


with open (file_name ,'r')as f :# Open file (read mode)
    data =f .read ()# Read string from file
    print (data )


    # ## 4.2 String processing

    # ### 4.2.1 Splitting a string: `split()`

    # [Chapter 4: Page 138]

    # In[ ]:


"에스프레소,아메리카노,카페라테,카푸치노".split (',')


# In[ ]:


"  에스프레소 아메리카노   카페라테      카푸치노\n".split ()


# ### 4.2.2 Removing unnecessary strings: `strip()`

# [Chapter 4: Page 139]

# In[ ]:


"aaaaPythonaaa".strip ('a')


# In[ ]:


"\n  Python  \n\n".strip ()


# ### 4.2.3 Concatenating strings: `join()`

# [Chapter 4: Page 140]

# In[ ]:


" ".join (["서울시","서초구","반포대로","201(반포동)"])


# In[ ]:


"****".join (["서울시","서초구","반포대로","201(반포동)"])


# In[ ]:


joined_str ="\n".join (["서울시","서초구","반포대로","201(반포동)"])
joined_str 


# In[ ]:


print (joined_str )


# ### 4.2.4 Finding strings: `find()`, `count()`, `startswith()`, `endswith()`

# [Chapter 4: Page 141]

# In[ ]:


str_p ="Python is powerful. Python is easy."

print (str_p .find ("Python"))# full range
print (str_p .find ("Python",10 ,30 ))# Specify start and end range
print (str_p .find ("easy"))# full range
print (str_p .find ("Python",21 ))# Specify starting range.No string matches
print (str_p .find ("Jupyter"))# Full range.No string matches


# [Chapter 4: Page 142]

# In[ ]:


print (str_p .count ("Python"))# full range
print (str_p .count ("Python",10 ,30 ))# Specify start and end range
print (str_p .count ("easy"))# full range
print (str_p .count ("Python",21 ))# Specify starting range.No string matches
print (str_p .count ("Jupyter"))# Full range.No string matches


# [Chapter 4: Page 143]

# In[ ]:


print ("- 문자열이 'Python'으로 시작?",str_p .startswith ("Python"))
print ("- 문자열이 'powerful'로 시작?",str_p .startswith ("powerful"))
print ("- 지정 범위에서 'powerful'로 시작?",str_p .startswith ("powerful",10 ))
print ("- 문자열이 'easy.'으로 끝?",str_p .endswith ("easy."))


# ### 4.2.5 String replacement: `replace()`

# [Chapter 4: Page 143]

# In[ ]:


str_o ="Python is powerful. Python is easy. Python is open."
print (str_o .replace ("Python","IPython"))# full range
print (str_o .replace ("Python","IPython",2 ))# Specify number of times


# ### 4.2.6 Changing case: `lower()`, `upper()`

# [Chapter 4: Page 144]

# In[ ]:


str_lu ="Python is powerful. PYTHON IS EASY."
print (str_lu .lower ())# Convert a string to all lowercase
print (str_lu .upper ())# Convert a string to all uppercase letters


# ## 4.3 Summary

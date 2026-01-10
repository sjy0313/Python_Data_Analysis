# !/usr/bin/env python
# coding: utf-8

# # Get from database

# <table class="tfo-notebook-buttons" align="left">
# <td>
# <a target="_blank" href="https://nbviewer.jupyter.org/github/rickiepark/hg-da/blob/main/Appendix-A.ipynb"><img src="https://jupyter.org/assets/share.png" width="61" />View with Jupyter Notebook Viewer</a>
# </td>
# <td>
# <a target="_blank" href="https://colab.research.google.com/github/rickiepark/hg-da/blob/main/Appendix-A.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />Running on Google Colab</a>
# </td>
# </table>

# ## Using SQL in Python: SQLite

# In[1]:


# The latest sqlalchemy causes an error in pandas.Please use version 1.4.*.(https://github.com/pandas-dev/pandas/issues/40686)
get_ipython ().system ('pip install -U sqlalchemy==1.4.46')


# In[2]:


import sqlite3 


# In[3]:


conn =sqlite3 .connect ('ns_lib.db')


# In[4]:


import gdown 

gdown .download ('https://bit.ly/3RhoNho','ns_202104.csv',quiet =False )


# **If there is a previously created nslib_book table, please delete it first.**

# In[5]:


c =conn .cursor ()

c .execute ("CREATE TABLE nslib_book \
          (name TEXT, author TEXT, borrow_count INTEGER)")


# In[6]:


c .execute ("CREATE TABLE IF NOT EXISTS nslib_book \
          (name TEXT, author TEXT, borrow_count INTEGER)")


# In[7]:


c .execute ("DROP TABLE nslib_book")


# In[8]:


c .execute ("CREATE TABLE nslib_book \
          (name TEXT, author TEXT, borrow_count INTEGER)")


# ## Adding data frame data to table

# In[9]:


import pandas as pd 

ns_df =pd .read_csv ('ns_202104.csv',low_memory =False )
ns_df .head ()


# In[10]:


for index ,row in ns_df .iterrows ():
    c .execute ("INSERT INTO nslib_book (name,author,borrow_count) \
              VALUES (?,?,?)",(row ['도서명'],row ['저자'],row ['대출건수']))


    # In[11]:


for index ,row in ns_df .iterrows ():
    pass 


    # In[12]:


book_df =ns_df [['도서명','저자','대출건수']]
book_df .head ()


# In[13]:


book_df .columns =['name','author','borrow_count']
book_df .head ()


# In[14]:


book_df .to_sql ('nslib_book',conn ,if_exists ='replace',index =False )


# ## Read data from table with Python

# In[15]:


c .execute ("SELECT * FROM nslib_book")


# In[16]:


c .fetchone ()


# In[17]:


c .fetchone ()


# In[18]:


c .fetchmany (3 )


# In[19]:


all_rows =c .fetchall ()


# In[20]:


book_df =pd .DataFrame (all_rows )
book_df .head ()


# In[21]:


book_df =pd .read_sql_query ("SELECT * FROM nslib_book",conn )
book_df .head ()


# In[22]:


book_df =pd .read_sql_table ('nslib_book','sqlite:///ns_lib.db')
book_df .head ()


# ## Obtaining statistics using functions provided by the database

# In[23]:


len (book_df )


# In[24]:


c .execute ("SELECT count(*) FROM nslib_book")
c .fetchone ()


# In[25]:


c .execute ("SELECT sum(borrow_count) FROM nslib_book")
c .fetchone ()


# In[26]:


c .execute ("SELECT avg(borrow_count) FROM nslib_book")
c .fetchone ()


# ## Sorting table data

# In[27]:


c .execute ("SELECT * FROM nslib_book ORDER BY borrow_count DESC LIMIT 10")
c .fetchall ()


# In[28]:


c .close ()
conn .close ()


# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 09:19:22 2024

@author: Solero
"""

# %%

# Example using SQLAlchemy

# pip install sqlalchemy
# pip install pymysql

# %%

import pandas as pd 
from sqlalchemy import create_engine 

# %%

# Database connection URL format
# DATABASE_URL = 'mysql+pymysql://username:password@localhost:3306/database'
DATABASE_URL ='mysql+pymysql://root:solsql@localhost:3306/hellodb'
engine =create_engine (DATABASE_URL )

# %%

# SQL query definition
sql ="SELECT * FROM hello"

hello_df =pd .read_sql_query (sql ,engine )
print (hello_df )

# %%

# THE END
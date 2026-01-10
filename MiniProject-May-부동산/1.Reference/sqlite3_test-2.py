# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:20:32 2024

@author: Shin
"""

import sqlite3 
# Connecting to sqlite database---(*1)
filepath ="test2.sqlite"
conn =sqlite3 .connect (filepath )

# Create a table and insert data ---(*2)
cur =conn .cursor ()
cur .execute ("DROP TABLE IF EXISTS items")
cur .execute ('''CREATE TABLE items (
item_id INTEGER PRIMARY KEY,
name TEXT,
price INTEGER) ''')
conn .commit ()
# Enter data ---(*3)
cur =conn .cursor ()# Since the purpose of creating the cursor is different, it must be executed separately each time.
# Select only name and price as columns.
cur .execute (
"INSERT INTO items (name,price) VALUES (?,?)",
("Orange",5200 ))
conn .commit ()

# Inserting multiple data in succession ---(*4)
# Import data using the data sql statement Import it as csv
# Automatic collection of learning data (modularized by building a database with scenarios for each age group)
# Scenario: By age (20s, 30s, 40s, 50s, 60s)
# - Virtual character
'''
Combination A: 20s to 30s
- Preferred infrastructure: transportation, leisure
- Asset holding status: 50 million ~ 100 million won
(1) Kim: “I am an office worker, I prefer a place close to a subway station, and sometimes I like to play screen golf or go to the gym.”
(2) Lee: “I am a self-employed person, and I want to have a house right next to the store (in a downtown area). I want to spend a lot of time alone, so I want to go hiking.”
(3) Park: “I am a freelancer, and I sometimes have client meetings, so I prefer a place close to a subway station, and it would be nice to be able to have a drink sometimes.”

Combination B: 30s to 40s
- Preferred infrastructure: schools, transportation, leisure
- Asset holding status: 200 million ~ 500 million won
(1) Oh: “I am married and my child is 2 years old. I prefer a place close to a kindergarten, and I hope there are good playgrounds and community facilities where my child can play.”
(2) Last name: “I’m single, and I want to live in a neighborhood with lots of good restaurants and bars.”
(3) Jang: “I live with my parents, but they are sick and I have to take them to the hospital, so I hope it’s somewhere close to the hospital.”

Combination C: 40s to 50s
- Preferred infrastructure: schools, hospitals, transportation
- Asset holding status: KRW 600 million ~ KRW 1 billion
(1) Sim: “I am a dual-income family, and my child is in middle school. I wish it were close to a middle school, and it would be nice if there was a restaurant close by where I could go out to eat occasionally.”
(2) Bae: “I am a single-income family, and my husband/wife works as a freelancer, so I would like a place with convenient transportation.”
(3) Ha: “I live with my parents, and sometimes when they are unwell, I have to take them to the hospital, so it would be nice if it were close to the hospital.”

Combination D: 50s to 60s
- Preferred infrastructure: hospitals, parks
- Asset holding status: KRW 1.1 billion ~ KRW 2 billion
(1) Chu: “The kids are all independent, and my husband (wife) said it would be nice to live next to XX Park, which is close to the gateball stadium, so I want to move there. The square footage doesn’t have to be large, just a square footage suitable for two people to live in.”
(2) Joe: “I am a single person who is sick, and it is very difficult to go to the hospital alone. I wish I could walk to the hospital and there would be no uphill or downhill roads.”
(3) Seo: “I have lost my husband/wife and am in good health, so I would like to live in an urban area close to a weekend farm.”
'''
cur =conn .cursor ()
data =[("Mango",7700 ),("Kiwi",4000 ),("Grape",8000 ),
("Peach",9400 ),("Persimmon",7000 ),('Banana',4000 )]
cur .executemany (
"INSERT INTO items (name,price) VALUES (?,?)",
data )
conn .commit ()

# Extract data between 4,000 and 7,000 won---(*5)
cur =conn .cursor ()
price_range =(4000 ,7000 )
cur .execute (
"SELECT * FROM items WHERE price>=? AND price<=?",
price_range )
cur .execute ("SELECT item_id,name,price FROM items ORDER BY price DESC LIMIT 5")
fr_list =cur .fetchall ()
for fr in fr_list :
    print (fr )


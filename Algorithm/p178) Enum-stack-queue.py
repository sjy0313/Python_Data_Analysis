# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 10:00:52 2024

@author: Shin
"""
# Stacks and Queues p 178
from enum import Enum 
# You can think of it as defining a type (class) called Menu.

Menu =Enum ('Menu',['인큐','디큐','피크','검색','덤프','종료'])

print (Menu .인큐 .name )# inq
print (Menu .덤프 .name )# dump

print (Menu .인큐 .value )# 1
print (Menu .덤프 .value )# 5
# Can be derived without using a class. Refer to p56enum.py.
# Printed even if Menu is not defined (because Enum was imported).
for menu in Menu :
    print ("{} : {}".format (menu .name ,menu .value ))
'''
Enqueue: 1
DQ: 2
Peak: 3
Search: 4
Dump: 5
Ends: 6
'''
# %%
import random 

def select_menu ()->Menu :# -> The return type of the above function is Menu.
# 
# It has no particular meaning.
    s =[f'({m .value }){m .name }'for m in Menu ]
    print (*s ,sep ='   ')
    n =random .randint (1 ,6 )
    return Menu (n )
    # Argument: Menu / Return: None
def print_menu (menu :Menu )->None :# The argument of the lowercase menu type is Menu.
    print ("[print_menu]{} : {}".format (menu .name ,menu .value ))


    # %%
menu =select_menu ()
print (menu )
print_menu (menu )# [print_menu]Peak: 3
# ['(1)InQ', '(2)DQ', '(3)Peak', '(4)Search', '(5)Dump', '(6)End']


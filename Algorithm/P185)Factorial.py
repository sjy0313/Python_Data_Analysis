# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:51:33 2024

@author: Shin
"""
# Use recursive calls when you need to find and process data
# 5!= 1*2*3*4*5 =120
# Finding the factorial of a positive integer
# argument, return = integer
def factorial (n :int )->int :
    t =1 

    print ("{}".format (1 ))

    while (n >1 ):# 5,4,3,2
        t *=n 
        print ("* {} = {}".format (n ,t ))
        n -=1 
        print ("* {}".format (1 ))
    return t 

if __name__ =='__main__':
    n =int (input ('출력할 팩토리얼 값을 입력하세요.:'))
    print (f'{n }의 팩토리얼은 {factorial (n )}입니다.')

    # %%
def factorial (n :int )->int :

    print ("[factorial] n: {}".format (n ))
    # 5,4,3,2
    if n <=1 :# n:1
        return 1 

    return n *factorial (n -1 )

if __name__ =='__main__':
    n =int (input ('출력할 팩토리얼 값을 입력하세요.:'))
    print (f'{n }의 팩토리얼은 {factorial (n )}입니다.')
'''
[factorial] n: 5
[factorial] n: 4
[factorial] n: 3
[factorial] n: 2
[factorial] n: 1
The factorial of 5 is 120.
'''



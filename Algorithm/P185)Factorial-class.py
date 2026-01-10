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
class Factoriral :
    def __init__ (self ,n :int ):
        self .__n =n # Property: Factorial value to calculate
        # internal method
    def __factorial (self ,x :int )->int :
        if x <=1 :
            return 1 

        return x *self .__factorial (x -1 )
        # public method (separate variable and method)
    def compute (self ):
        return self .__factorial (self .__n )

n =5 
factobj =Factoriral (n )

result =factobj .compute ()


# AttributeError: 'Factoriral' object has no attribute '__n'
# print(f'The factorial of {n},{factobj.__n} is {result}.')
# Specifies __ that prevents access to object internal properties from outside the object.(private = __)

print (f'{n }의 팩토리얼은 {factorial (n )}입니다.')



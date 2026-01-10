# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:16:18 2024

@author: Shin
"""
# algorithm

import random 
n =int (input ('난수 개수입력: '))

for _ in range (n ):# _ means that only 0 to n-1 counts will be processed.
    r =random .randint (10 ,99 )
    print (r ,end =' ')
    if r ==20 :
        print ('\n당첨을 축하합니다')
        break 
else :# If the for statement does not end with a break, it is processed.
    print ('\n난수의 생성을 종료')


    # itertools.permutation(iterable, r= None) Among 46 iterable objects
    # A function that returns the permutation of r selections
import itertools 
list (itertools .permutations (range (1 ,46 ),6 ))
# There are too many cases so printing is not possible.
# You can implement the permutation function using a for statement, but the code becomes long.
# Therefore, use permutation()

import itertools 
lotto =itertools .combinations (range (1 ,46 ),6 )
for num in lotto :
    print (num )
    # On the other hand, if combination is used, six duplicate combinations are excluded.
    # itertools.combinations_with_replacement()
    # The above is a combination that allows for duplicate numbers (duplicate combination).
len (list (itertools .combinations_with_replacement (range (1 ,46 ),6 )))
# Number of cases: 15890700.




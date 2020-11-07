# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:08:23 2019


"""

import numpy as np 

def rec(n):
    if n == 1:
        return n
    else:
        return n*rec(n-1)
    


a = int(5)
array = np.empty(a)

for i in range (5):
    array[i] = int(input("Enter Number:"))
    
for i in range(5):
    if array[i] < 0:
        print("Invalid")
        
    elif array[i] == 0:
        print("The factorial of",array[i] , "is: 1 ")
        
    else:
        print("The factorial of",array[i] , "is: " , rec(array[i]))
        
    
    

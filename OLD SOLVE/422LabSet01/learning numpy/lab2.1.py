# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 15:34:43 2019

@author: HP
"""
import numpy as np
    
def factorial( n ):
   if n <1:   # base case
       return 1
   else:
       returnNumber = n * factorial( n - 1 )  # recursive call
      
       return returnNumber

a=np.zeros(5)
for i in np.arange(0,5):
    a[i]=int(input("Enter number"))
for i in np.arange(0,5):
    print("Factorial of ",a[i]," is ",factorial(a[i]))
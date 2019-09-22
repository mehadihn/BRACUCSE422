# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 12:13:57 2019

@author: 17101177
"""


add = 0
counter  = 0
 
for x  in range (1 , 100):
     if (x % 3 == 0):
         #print (x)
         add = add + x
         counter += 1

        
print ("Average:" , (add/counter))
         
         
     
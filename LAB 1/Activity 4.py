# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 12:09:37 2019

@author: 17101177
"""

i = int(input("Enter number of Copies: "))

if i <= 100:
    print ("Total Cost: " , (i*50))
    
else: 
    extra = i - 100
    total = (100 * 50) + (extra * 30)
    print ("Total Cost: " , total)
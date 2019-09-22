# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 11:45:28 2019

@author: 17101177
"""

i = int(input("Enter number of Inches: "))

j = i / 12 
k = j % 10

#print (j , "  " , k)
print ( i , " inches is " , round(j , 0 ) , " feet and " , round (5,0), " inches")
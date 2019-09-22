# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 13:07:55 2019

@author: 17101177
"""

a = int(input("Enter a year:"))

if (a%4==0):
    if(a % 100 == 0):
        if (a % 400 == 0):
            print ("Leap year")
            
        else:
            print ("Not a leap year")
    
    else:
        print ("Leap Year")
        
else:
    print("Not a leap year")
    
    

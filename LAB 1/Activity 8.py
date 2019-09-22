# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 13:04:08 2019

@author: 17101177
"""

i = [ 56, 78 , 96 , 74 , 2 , 58]

small = i[0]
large = i[0]

for a in i:
    if a > large:
        large = a
        
for a in i:
    if a < small:
        small = a
        
print ("Sum of Small and Large: " , small + large)
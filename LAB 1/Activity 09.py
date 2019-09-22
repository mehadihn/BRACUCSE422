# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 12:26:49 2019

@author: 17101177
"""

#9. Make a list with 10 numbers and print: 
    #(a) the difference between average number and smallest number, and 
    #(b) difference between average and largest number. 
    
    
i = [25, 26 , 7, 45, 68, 78, 45, 79 , 71, 30]

small = i[0]
large = i[0]

for a in i:
    if a > large:
        large = a
        
for a in i:
    if a < small:
        small = a
        
add = 0
for a in i:
    add = add + a
    
avg = add / len(i)
diffL = large -avg
diffS = avg - small 
print("the difference between average number and smallest number: ", diffS)
print("difference between average and largest number " , diffL)


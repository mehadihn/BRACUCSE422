# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 09:38:36 2019

@author: Mehadi Hassan
"""

s1 = input("String 1: ")
s2 = input("String 2: ")

if(len(s1) != len(s2)):
    print("String Size Do not Match")
else:
    count = 0

    for x in range(len(s1)):
        if s1[x] != s2[x]:
            count = count + 1
       
    print("Hamming Distance is: ", count)

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time

start = time.time()

n = 27

def hailstone(a):
    print(a)
    if a != 1:
        if a %2 == 0:
            hailstone(a/2)
        else:
            hailstone(3*a + 1)
            

hailstone(n)

print("Time Required: " ,(time.time() - start))
         
    
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 20:22:53 2019

@author: Mehadi Hassan
"""
import math

def pyramid_AV(n , s , h):
    a = (1/2)*s*(1/math.tan(math.pi/n))
    A = (1/2)*n*s*a
    l = math.sqrt(h*h+a*a)
    
    
    V = (1/3)*A*h
    S = A + (1/2)*n*s*l
    return V , S

V , S = pyramid_AV(3,6,3)

print(V)
print(S)

          
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 19:58:02 2019

@author: Mehadi Hassan
"""

import numpy as np

def dot(a,b):
    print("a.b=")
    print(np.dot(a,b))
    print()
    
def cross(a,b):
    print("aXb=")
    print(np.cross(a,b))
    print()

def sTriple(a,b,c):
    print("a.(bXc)=")
    print(np.dot(a,np.cross(b,c)))
    print()

def vTriple(a,b,c):
    print("aX(bXc)=")
    print(np.cross(a, np.cross(b,c)))
    print()
    
    
    
a = np.array([81,12,63])
b = np.array([14,15,36])
c = np.array([57,82,39])
#a = np.random.rand(3,3)
#b = np.random.rand(3,3)
dot(a,b)
cross(a,b)
sTriple(a,b,c)
vTriple(a,b,c)
    
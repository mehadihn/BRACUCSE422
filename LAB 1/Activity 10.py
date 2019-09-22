# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 12:42:30 2019

@author: 17101177
"""
import math
a = int(input("Enter First Value: "))
b = int(input("Enter Second Value: "))
c = int(input("Enter Third Value: "))

s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print ("Area of triangle: " , area)
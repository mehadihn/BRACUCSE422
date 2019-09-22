# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 12:51:40 2019

@author: 17101177
"""

import math
##Hints: It forms a quadratic equation X^2-X-1980=0
a = 1
b = -1
c = -1980
vsqrt = math.sqrt((b*b) - (4*a*c))

ansP = (-1*b + vsqrt)/(2*a)
ansN = (-1*b - vsqrt)/(2*a)

print("Value of X: " , ansP)
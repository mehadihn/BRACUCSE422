# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:26:26 2019

@author: 17101177
"""

import numpy as np

a = np.zeros(10)
b = np.ones(10)
A = a.reshape(5,2)
B = b.reshape(5,2)
print(np.concatenate([A,B] , axis = 0))
print()
print(np.concatenate([A,B] , axis = 1))
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 15:56:03 2019

@author: HP

"""
import numpy as np
data = np.genfromtxt("task 3.txt", delimiter=',', skip_header=1, filling_values=-999, dtype='float')
print(data)

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 15:07:27 2019

@author: HP
"""

import numpy as np
x = np.zeros(10)
y= np.ones(10)
z=x.reshape(2,5)
k=y.reshape(2,5)
print(np.concatenate([x, y]))
p=np.concatenate([z, k])
print(p)
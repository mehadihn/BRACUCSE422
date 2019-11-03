# -*- coding: utf-8 -*-


import numpy as np
m = np.zeros(10)
n= np.ones(10)
o=m.reshape(2,5)
x=n.reshape(2,5)

print(np.concatenate([m, n]))

value=np.concatenate([o, x])
print(value)
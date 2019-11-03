# -*- coding: utf-8 -*-

import numpy as np
readfile = np.genfromtxt("readfile lab2 task 3.txt", delimiter=',', skip_header=1, filling_values=-999, dtype='float')
print(readfile)

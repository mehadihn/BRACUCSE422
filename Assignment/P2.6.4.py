# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 14:49:39 2019

@author: Mehadi Hassan
"""
import numpy as np
a = open("ABCD.txt")
listA = []
#line = a.readlines()
while True:
    list = a.readline()
    list = list.split()
    listA.append(list)
#    print(list)
    if not list:
        listA.remove([])
        break
a.close()
print(listA)
x = np.array(listA)
#print(x)
l = []
for i in range(x.shape[1]):
    j = 0
    k = []
    while(j!=x.shape[0]):
        k.append(x[j , i])
        j = j+1
    
    l.append(k)
print(l)



      




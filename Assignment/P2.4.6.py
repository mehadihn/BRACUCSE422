# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 10:58:11 2019

@author: Mehadi Hassan
"""

n = int(input("Enter A Number: "))

if n==0:
    print("n!! = " ,1)



elif n%2==0:
    l = int((n/2))
    doubleFact = 1
    for i in range (l):
       doubleFact = doubleFact*  n
       n = n-2 
    
    print("n!! = " ,doubleFact)

else:
    l = int((n+1)/2)
    
    doubleFact = 1
    for i in range (l):
        doubleFact = doubleFact*  n
        n = n-2
    print("n!! = " ,doubleFact)
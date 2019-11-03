#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 14:27:33 2019

@author: mehadi
"""
    
word = ["ki" , "khobor"]

def sensor(text):
    li = list(text.split())
    
    print(li)
    #print(word)
    for i in range (len(li)):
        for j in range (len(word)):
            if li[i] == word[j]:
                text =  text.replace(word[j] , '*' * len(word[j]))
                #print("Replaced: " , word[j])
    return text
    
print (sensor("Hi ki khobor tomader"))
    
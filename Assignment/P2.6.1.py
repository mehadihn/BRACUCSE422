#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 13:48:51 2019

@author: mehadi
"""

import pandas as pd

data = pd.read_csv('redwood-data.csv' , usecols = ['diameter (m)' , 'height (m)'])

print("Tallest Tree: ", max(data['height (m)']))
print("The tree with the greatest diameter:" , max(data['diameter (m)']))
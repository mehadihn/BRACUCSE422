# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 22:15:12 2019

@author: Mehadi Hassan
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import networkx as nx

G = nx.Graph()
data = pd.read_csv('path.csv' , delimiter  = ',')

start = data.columns[0]
dest = data.columns[1]
island = data.columns[2]

for i in range(1,len(data),1):
    G.add_edge(data[start][i], data[dest][i], weight=data[island][i])
    
#A* Search
print("Optimal Route Between",start , "& Destination",dest,":")
print(nx.astar_path(G, start, dest, heuristic=None, weight='weight'))





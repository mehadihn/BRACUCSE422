# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
data = pd.read_csv('path.csv' , delimiter  = ',')

start = data.columns[0]
dest = data.columns[1]
island = data.columns[2]

for i in range(1,len(data),1):
    #print(data[start][i], data[dest][i], data[island][i])
    G.add_edge(data[start][i], data[dest][i], weight=data[island][i])
#print(G.nodes())
#nx.draw(G)
#path = nx.shortest_path(G, source='A', target='Z')
#print(path)


total, path = nx.single_source_dijkstra(G, source='A', target='Z')
print(path)
print(total)
#ix =[[path[i],path[i+1]] for i in range(len(path)-1)]
#total = sum([m[i[0]][i[1]] for i in ix])
    
#A* Search
#print(nx.astar_path(G, 'A', 'Q', heuristic=None, weight='weight'))


#for i in range(1, l ,1):
    #if graph[]
        #print("Yes")
        



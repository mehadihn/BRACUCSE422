import pandas as pd

data = pd.read_csv('path.csv' , delimiter  = ',')

start = data.columns[0]
dest = data.columns[1]
island = data.columns[2]

#Initializing Dictionaries with empty keys
adjList={}
for i in range(1,len(data),1):
    key = data[start][i]
    adjList.setdefault(key, [])
    key = data[dest][i]
    adjList.setdefault(key, [])

#Inputing Values to that coresponding keys
for i in range(1,len(data),1):
    adjList[data[start][i]].append((data[dest][i] , data[island][i]))
    adjList[data[dest][i]].append((data[start][i] , data[island][i]))

#Creating Heuristic
data = pd.read_csv('Heuristic.csv' , delimiter = ',')

heuristic = {}
heuristic[data.columns[0]] = int(data.columns[1])
#Initializing the dictionary with keys
for i in range(1,len(data),1):
    key = data[start][i]
    heuristic[key] = 1
#Adding values to the dictionary
for i in range(1,len(data),1):
    heuristic[data[start][i]] = data[data.columns[1]][i]

#Graph Class
class graph:
    #constructor
    def __init__(self, adjList, heuristic):
        self.adjList = adjList
        self.heuristic = heuristic
        print(adjList)
        print()
        print(heuristic)
        
    #returns neighbours of that node    
    def get_neighbors(self, node):
        return self.adjacency_list[node]
    
    def aStarSearch(self, startNode, destNode):
        print()

graph = graph(adjList , heuristic)        

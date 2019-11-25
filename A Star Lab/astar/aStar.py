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
    #adjLsit[key].append(1)

#print(adjList)

#Inputing Values to that coresponding keys
for i in range(1,len(data),1):
    adjList[data[start][i]].append((data[dest][i] , data[island][i]))
    adjList[data[dest][i]].append((data[start][i] , data[island][i]))
    
#print(adjList)
#graph1 = graph(adjList)


#Creating Heuristic
data = pd.read_csv('Heuristic.csv' , delimiter = ',')

heuristic = {}
temp = int(data.columns[1]) ## as it gives str so converting to int
heuristic.setdefault(data.columns[0], [temp])


for i in range(1,len(data),1):
    key = data[start][i]
    heuristic.setdefault(key, [])

for i in range(1,len(data),1):
    heuristic[data[data.columns[0]][i]].append(data[data.columns[1]][i])

#print(heuristic)


class graph:
    #constructing
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
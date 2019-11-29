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
    #print(adjList)
    adjList[data[start][i]].append((data[dest][i] , data[island][i]))
    adjList[data[dest][i]].append((data[start][i] , data[island][i]))
    #print(adjList)
#Creating Heuristic
data = pd.read_csv('Heuristic.csv' , delimiter = ',')

heuristic = {}
heuristic[data.columns[0]] = int(data.columns[1])
#Initializing the dictionary with keys
for i in range(0,len(data),1):
    key = data[start][i]
    heuristic[key] = 1
#Adding values to the dictionary
for i in range(0,len(data),1):
    heuristic[data[start][i]] = data[data.columns[1]][i]
    
#Graph Class
class graph:
    #constructor
    def __init__(self, adjList, heuristic):
        self.adjList = adjList
        self.heuristic = heuristic
        #print(adjList)
        #print()
        #print(heuristic)
        
    #returns neighbours of that node    
    def get_neighbors(self, node):
        return self.adjList[node]
    
    def aStarSearch(self, start, dest):
      print("Start Node:" ,start)
      print("Destination Node:" ,dest)
      openList = set([start])
      closeList = set([])
      
      distance = {}
      distance[start] = 0
      
      parents = {}
      parents[start] = start
      
      while len(openList)>0:
          node = None
          
          for v in openList:
              if node == None or (distance[v] + heuristic[v] < distance[node] + heuristic[node]):
                  node = v
                  
          if node  == None:
              print("Path Nai")
              return None
          
          if node == dest:
              path = []
              pathCost = 0
              while parents[node] != node:
                  path.append(node)
                  node = parents[node]
              
              path.append(start)
              path.reverse()
              
              for i in path:
                 print(adjList[i])
              
              
              
              print("Path is:", path)
              return path
          
          for(i , cost) in self.get_neighbors(node):
              
              if i not in openList and i not in closeList:
                  openList.add(i)
                  parents[i] = node
                  distance[i] = distance[node] + cost
                  
              else:
                  if distance[i] > distance[node] + cost:
                      distance[i] = distance[node] + cost
                      parents[i] = node
                      
                      if i in closeList:
                          closeList.remove(i)
                          openList.add(i)
                          
          openList.remove(node)
          closeList.add(node)                            
            
      print("Path Nai")
      return None              
              


graph = graph(adjList , heuristic) 
#print(graph.get_neighbors("D"))  
graph.aStarSearch('C','X')    
      


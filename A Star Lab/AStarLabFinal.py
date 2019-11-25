#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt


#from collections import deque

class Graph:


    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]
    
    
    def h(self, n):
       # a = DFS(self, n)
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1,
            'E':1,
            'P':1,
            'Q':1,
            'X':1,
            'Y':1,
            'Z':1
        }

        return H[n]
    
   
    

   # def DFSUtil(self, v, visited): 


     #   visited[v] = True
      #  print(v, end = ' ') 


       # for i in self.graph[v]: 
      #      if visited[i] == False: 
       #         self.DFSUtil(i, visited) 

  #  def DFS(self, v): 

  #    visited = [False] * (len(self.graph))


      #  self.DFSUtil(v, visited) 




    def a_star_algorithm(self, start_node, stop_node):

        open_list = set([start_node])
        closed_list = set([])


        g = {}

        g[start_node] = 0


        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None


            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None


            if n == stop_node:
                    reconst_path = []
    
                    while parents[n] != n:
                        reconst_path.append(n)
                        n = parents[n]
    
                    reconst_path.append(start_node)
    
                    reconst_path.reverse()
    
                    print('Path found: {}'.format(reconst_path))
                    return reconst_path


            for (m, weight) in self.get_neighbors(n):


                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)


            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None
    
    

adjacency_list={
        'A':[('C',10),('B',20)],
        'B':[('C',50),('D',51),('E',32)],
        'C':[('A',10),('B',50)],
        'D':[('P',21),('Q',30),('B',51)],
        'E':[('P',10),('Q',11),('B',32)],
        'P':[('X',11),('Y',12),('D',21),('E',10)],
        'Q':[('Z',72),('D',30),('E',11)],
        'X':[('Z',21),('P',11)],
        'Y':[('Z',50),('P',12)],
        'Z':[('Q',72),('X',21),('Y',50)],
    }

graph1 = Graph(adjacency_list)
graph1.a_star_algorithm('A', 'X')
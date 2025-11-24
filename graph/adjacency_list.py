from collections import defaultdict

class Graph:
    def __init__(self, nodes):
        self.graph = defaultdict(list)

    def add_edge(self,i,j,weight):
        self.graph[i].append([j,weight]) # you can also using tuple instead of list
        # self.graph[j].append([i,weight]) # uncomment if you want the graph to be undirected

    def print(self):
        print(self.graph)

# directed graph
g = Graph(4)
g.add_edge(0,1,5)
g.add_edge(0,2,3)
g.add_edge(1,2,2)
g.add_edge(2,0,1)
g.add_edge(2,3,4)
g.add_edge(3,3,7)

g.print()

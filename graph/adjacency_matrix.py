class Graph:
    def __init__(self, nodes, is_directed):
        self.nodes = nodes
        self.graph = [ [0]*self.nodes for _ in range(self.nodes)]
        self.is_directed = is_directed

    def add_edge(self,i,j,weight):
        self.graph[i][j]=weight
        if not self.is_directed:
            self.graph[j][i]=weight

    def add_node(self):
        self.nodes += 1
        for i in self.graph:
            i.append(0)
        self.graph.append([0]*self.nodes)

    def __str__(self):
        a = ""
        for i in self.graph:
            a += f"{i}\n"
        return a

# directed graph
g = Graph(nodes=4, is_directed=True)
g.add_edge(0,1,5)
g.add_edge(0,2,3)
print(g)
g.add_node()
g.add_edge(1,2,2)
g.add_edge(2,0,1)
g.add_edge(2,3,4)
g.add_edge(3,3,7)
g.add_edge(0,4,4)
print(g)



# v = 4
# edge = [[0,1,5],[0,2,3],[1,2,2],[2,0,1],[2,3,4],[3,3,7]] # edge List
#
# def createAdjMatrix(edge):
#     adjMatrix = [ [ 0 for _ in range(v)] for _ in range(v)]
#     for e in edge:
#         adjMatrix[e[0]][e[1]] = e[2]
#
#     return adjMatrix
#
# adjMatrix = createAdjMatrix(edge)
#
# for i in adjMatrix:
#     print(i)

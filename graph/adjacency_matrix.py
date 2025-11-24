class Graph:
    def __init__(self, nodes):
        self.graph = [ [0]*nodes for _ in range(nodes)]

    def add_edge(self,i,j,weight):
        self.graph[i][j]=weight

    def __str__(self):
        a = ""
        for i in self.graph:
            a += f"{i}\n"
        return a

g = Graph(4)
g.add_edge(0,1,5)
g.add_edge(0,2,3)
g.add_edge(1,2,2)
g.add_edge(2,0,1)
g.add_edge(2,3,4)
g.add_edge(3,3,7)

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

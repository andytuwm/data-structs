__author__ = 'Andy'


class Node:
    def __init__(self, key):
        self.connections = {}
        self.key = key

    def addNeighbour(self, node, weight=0):
        self.connections[node.key] = weight

    def getNeighbours(self):
        return self.connections.keys()

    def getKey(self):
        return self.key

    def getNeighbourWeight(self, neighbour):
        return self.connections[neighbour]


class AdjacencyListGraph:
    def __init__(self):
        self.vertexList = {}
        self.vertices = 0

    def addVertex(self, key):
        self.vertices += 1
        newVert = Node(key)
        self.vertexList[key] = newVert
        return newVert

    def getVertex(self, key):
        if key in self.vertexList.keys():
            return self.vertexList[key]
        else:
            return None

    def addEdge(self, vfrom, vto, weight):
        if vfrom.getKey() not in self.vertexList.keys():
            vfrom = self.addVertex(vfrom.key)
        if vto.getKey() not in self.vertexList.keys():
            vto = self.addVertex(vto.key)
        vfrom.addNeighbour(vto, weight)

    def getVertices(self):
        return self.vertexList.keys()

    def __iter__(self):
        return iter(self.vertexList.values())


def BFSconnected(graph, startkey, endkey):
    path = set()
    queue = []
    queue.append(startkey)
    while len(queue) > 0:
        currKey = queue.pop(0)
        if currKey == endkey: return True
        currNode = graph.getVertex(currKey)
        neighbourKeys = currNode.getNeighbours()
        for k in neighbourKeys:
            if k not in path:
                queue.append(k)
                path.add(k)
    return False


def DFSconnected(graph, startkey, endkey):
    path = set()
    stack = []
    stack.append(startkey)
    while len(stack) > 0:
        currKey = stack.pop()
        if currKey == endkey: return True
        currNode = graph.getVertex(currKey)
        neighbourKeys = currNode.getNeighbours()
        for k in neighbourKeys:
            if k not in path:
                stack.append(k)
                path.add(k)
    return False


graph = AdjacencyListGraph()
v1 = graph.addVertex(1)
v4 = graph.addVertex(4)
v3 = graph.addVertex(3)
v2 = graph.addVertex(2)
print(graph.getVertices())
graph.addEdge(v1, v4, 4)
graph.addEdge(graph.getVertex(1), v3, 7)
graph.addEdge(graph.getVertex(2), graph.getVertex(1), 2)
graph.addEdge(graph.getVertex(3), graph.getVertex(1), 6)
graph.addEdge(graph.getVertex(3), graph.getVertex(4), 8)
for x in graph:
    print(x.connections)
print(BFSconnected(graph, 2, 4))
print(BFSconnected(graph, 3, 2))

print(DFSconnected(graph, 2, 4))
print(DFSconnected(graph, 3, 2))

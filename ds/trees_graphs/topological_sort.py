'''
-> It is any ordering of all the graph vertices that satisfies all precedence relationships
Topological sort works only on Directed Acyclic Graph
If there is a cycle in Graph, then there is no topological sort

Implementation: -> Kahn's algorithm 

Comes After: A node comes after certain nodes
InDegree: No of incoming edges on a node

1. Calculate InDegree of all nodes in a graph
2. Pick InDegree of 0 node (indicates it can be processed) add to result set
3. Remove that node from Graph, alters indegree of all nodes
4. Repeat the same
5. All precedence relationships satisfied

Time Complexity: O(V+E), V->Vertex, E->Edge
Each edge is visited exactly once
Each vertex is visited exactly once
Multiple solutions possible
'''

from queue import Queue
from graph_adj_matrix import *


def topogical_sort(graph):

    queue = Queue()

    indegreeMap = {}

    for i in range(graph.numVertices):
        indegreeMap[i] = graph.get_indegree(i)

        if indegreeMap[i] == 0:
            queue.put(i)

    sortedList = []

    while not queue.empty():
        vertex = queue.get()
        sortedList.append(vertex)

        for v in graph.get_adjacent_vertices(vertex):
            indegreeMap[v] -= 1

            if indegreeMap[v] == 0:
                queue.put(v)

    if len(sortedList) != graph.numVertices:
        raise ValueError("This graph has a cycle!")

    print(sortedList)




if __name__ == "__main__":
    g = AdjacentMatrixGraph(9, directed=True)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 7)
    g.add_edge(2, 4)
    g.add_edge(2, 3)
    g.add_edge(1, 5)
    g.add_edge(5, 6)
    g.add_edge(3, 6)
    g.add_edge(3, 4)
    g.add_edge(6, 8)

    topogical_sort(g)


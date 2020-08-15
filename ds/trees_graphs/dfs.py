from queue import Queue
from graph_adj_matrix import *


def dfs(graph, visited, current=0):

    if visited[current] == 1:
        return

    visited[current] = 1
    print(f"Visit: {current}")

    for vertex in graph.get_adjacent_vertices(current):
        dfs(graph, visited, vertex)


def dfs_stack(graph, current=0):

    stack = []
    visited = []
    stack.append(current)

    while len(stack) > 0:
        current = stack.pop()
        if current not in visited:
            for vertex in graph.get_adjacent_vertices(current):
                if vertex not in visited:
                    stack.append(vertex)
            visited.append(current)

    return visited


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

    visited = np.zeros(g.numVertices)
    dfs(g, visited)

    print(dfs_stack(g))
    

'''
Its a greedy algorithm to find minimal spanning tree for a weighted undirected graph
The graph can be unconnected

Algorithm Steps:
1. Add edges to Priority Queue in Increasing order of weights
2. Initialise Empty Result Set
3. Find Short Edge which is not currently in the Result Set, Dequeue from Priority Queue
4. Reject if Cycle is introduced else add to Result Set
5. Stop when N-1 edges in the Result Set (n-number of vertices in graph)
'''


import priority_dict
from graph_adj_matrix import *


def spanning_tree(graph):

    priority_queue = priority_dict.priority_dict()

    for v in range(graph.numVertices):
        for neighbor in graph.get_adjacent_vertices(v):
            priority_queue[(v, neighbor)] = graph.get_edge_weight(v, neighbor)

    visited_vertices = set()
    spanning_tree = {}

    for v in range(graph.numVertices):
        spanning_tree[v] = set()

    num_edges = 0

    while len(priority_queue.keys()) > 0 and num_edges < graph.numVertices - 1:
        v1, v2 = priority_queue.pop_smallest()

        if v1 in spanning_tree[v2]:
            continue

        # helps in detecting cycles
        vertex_pair = sorted([v1, v2])

        spanning_tree[vertex_pair[0]].add(vertex_pair[1])

        if has_cycle(spanning_tree):
            spanning_tree[vertex_pair[0]].remove(vertex_pair[1])
            continue

        num_edges += 1

        visited_vertices.add(v1)
        visited_vertices.add(v2)

    print(f"Visited vertices: {visited_vertices}")

    if len(visited_vertices) != graph.numVertices:
        print("Minimum Spaning Tree not found")
    else:
        print("Minimum Spaninng Tree:")
        for key in spanning_tree:
            for value in spanning_tree[key]:
                print(f"{key}-->{value}")


def has_cycle(spanning_tree):

    for source in spanning_tree:
        q = []
        q.append(source)

        visited_vertices = set()

        while len(q) > 0:
            vertex = q.pop(0)

            if vertex in visited_vertices:
                return True

            visited_vertices.add(vertex)
            q.extend(spanning_tree[vertex])

    return False


if __name__ == "__main__":
    g = AdjacentMatrixGraph(8, directed=False)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 3, 2)
    g.add_edge(2, 3, 2)
    g.add_edge(1, 4, 3)
    g.add_edge(3, 5, 1)
    g.add_edge(5, 4, 2)
    g.add_edge(3, 6, 1)
    g.add_edge(6, 7, 1)
    g.add_edge(7, 0, 1)
        
    
    spanning_tree(g)








    

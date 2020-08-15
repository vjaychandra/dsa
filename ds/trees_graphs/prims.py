'''
Prims Algorithm to find Minimum Spanning Tree
Works only with Connected graph
It is a greedy algorithm to fing min spanning tree for a weighted undirected graph
Min Spanning Tree is a Forest of Disjoint Trees
'''


import priority_dict
from graph_adj_matrix import *


def spanning_tree(graph, source):

    distance_table = {}

    for i in range(graph.numVertices):
        distance_table[i] = (None, None)

    distance_table[source] = (0, source)

    priority_queue = priority_dict.priority_dict()
    priority_queue[source] = 0

    visited_vertices = set()
    spanning_tree = set()

    while len(priority_queue.keys()) > 0:

        current_vertex = priority_queue.pop_smallest()

        if current_vertex in visited_vertices:
            continue

        visited_vertices.add(current_vertex)

        if current_vertex != source:
            last_vertex = distance_table[current_vertex][1]

            edge = f"{last_vertex}-->{current_vertex}"
            if edge not in spanning_tree:
                spanning_tree.add(edge)

        for neighbor in graph.get_adjacent_vertices(current_vertex):
            distance = g.get_edge_weight(current_vertex, neighbor)
            neighbor_distance = distance_table[neighbor][0]

            if neighbor_distance is None or neighbor_distance > distance:
                distance_table[neighbor] = (distance, current_vertex)
                priority_queue[neighbor] = distance


    for edge in spanning_tree:
        print(edge)


if __name__ == "__main__":
    g = AdjacentMatrixGraph(8, directed=False)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 3, 2)
    g.add_edge(2, 3, 2)
    g.add_edge(1, 4, 3)
    g.add_edge(3, 5, 1)
    g.add_edge(5, 4, 3)
    g.add_edge(3, 6, 1)
    g.add_edge(6, 7, 1)
    g.add_edge(7, 0, 1)
        
    
    spanning_tree(g, 3)







                

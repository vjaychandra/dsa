from abstract_graph import Graph


class Node:
    def __init__(self, vertexId):
        self.vertexId = vertexId
        self.adjacency_set = set()

    def add_edge(self, v):
        if self.vertexId == v:
            raise ValueError(f"The vertex {v} cannot be adjacent to itelf")
        self.adjacency_set.add(v)

    def get_adjancency_vertices(self):
        return sorted(self.adjacency_set)


class AdjacencySetGraph(Graph):
    def __init__(self, numVertices, directed=False):
        super(AdjacencySetGraph, self).__init__(numVertices, directed)

        self.vertex_list = []
        for i in range(numVertices):
            self.vertex_list.append(Node(i))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError(f"Vertices {v1} and {v2} are out of bounds")

        if weight != 1:
            raise ValueError("An Adjacency set cannot represent edge weights > 1")

        self.vertex_list[v1].add_edge(v2)

        if not self.directed:
            self.vertex_list[v2].add_edge(v1)

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError(f"Cannot access vertex {v}")

        return self.vertex_list[v].get_adjancency_vertices()

    def get_indegree(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex {v}")

        indegree = 0
        for i in range(self.numVertices):
            if v in self.get_adjacent_vertices(i):
                indegree += 1
        return indegree

    def get_edge_weight(self, v1, v2):
        return 1

    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                print(f"{i} --> {v}")


if __name__ == "__main__":

    g = AdjacencySetGraph(4, directed=True)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(2, 3)

    for i in range(4):
        print(f"Adjacent to: {i} -> {g.get_adjacent_vertices(i)}")

    for i in  range(4):
        print(f"Indegree: {i} -> {g.get_indegree(i)}")

    g.display()    

            




    
    

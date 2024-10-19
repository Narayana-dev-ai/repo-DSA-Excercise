class Graph:
    def __init__(self, size):
        self.size = size
        self.vertex = [''] * size
        self.adj_matrix = [[0] * size for _ in range(size)]
        
        
    def add_edge(self, u , v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1
            
    def add_vertex(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex[vertex] = data
        
    def print_graph(self):
        print("Adjacency Matrxi: ")
        for i in self.adj_matrix:
            print(" ".join(map(str, i)))
            
        print("\nVertex Data")
        for vertex, data in enumerate(self.vertex):
            print(f"Vertex {vertex}: {data}")
    
    
g = Graph(4)
g.add_vertex(0, 'A')
g.add_vertex(1, 'B')
g.add_vertex(2, 'C')
g.add_vertex(3, 'D')
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 2)

g.print_graph()
class Graph:
    def __init__(self):
        self.graph = {}
    def add_vertex(self, data):
        self.graph[data] = []
    def insert(self,vertex, edge, is_bidirectional):
        if vertex not in self.graph:
            self.add_vertex(vertex)

        if edge not in self.graph:
            self.add_vertex(edge)

        self.graph[vertex].append(edge)
        if is_bidirectional:
            self.graph[edge].append(vertex)

    def display(self):
        for key, values in self.graph.items():
            print(key, "->", values)



gh = Graph()
gh.insert(3, 5, True)
gh.insert(3, 4, True)
gh.insert(5, 6, False)
gh.display()




def connect_vertex(vertex1, vertex2, weight=1):
    edge = Edge(vertex1, vertex2, weight)

    vertex1.edges.append(edge)
    vertex2.edges.append(edge)


def find_vertex(num):
    def f(vertex):
        return vertex.data == num
    return f


class Graph:
    def __init__(self):
        self.vertexes = []

    def add_vertex(self, vertex):
        self.vertexes.append(vertex)

    def print_graph(self):
        print(self)

    def __str__(self):
        result = ''
        for vertex in self.vertexes:
            result += f" {vertex}"
        return result

    def find_shortest_path(self, start, end):
        queue = [start]

        distances = {
            start: 0
        }

        for vertex in self.vertexes:
            if vertex in distances:
                continue

            distances[vertex] = 2 ** 62

        while len(queue) > 0:
            current = queue.pop(0)
            fuc = current.neighbors_with_weights()

            for neigh, weight in fuc.items():
                curr_weight = distances[neigh]
                new_weight = distances[current] + weight
                print(curr_weight, new_weight, neigh)

                if curr_weight < new_weight:
                    distances[neigh] = curr_weight
                else:
                    distances[neigh] = new_weight




        print(distances)



    def dfs(self, func):
        visited = set()

        def recursive_dfs(vertex):
            print(vertex.data)
            visited.add(vertex)

            if func(vertex):
                return True

            for edge in vertex.edges:
                next_vertex = None

                if vertex != edge.vertex1:
                    next_vertex = edge.vertex1

                else:
                    next_vertex = edge.vertex2

                if next_vertex not in visited:
                    if recursive_dfs(next_vertex):
                        break
            return False
        recursive_dfs(self.vertexes[0])


class Vertex:
    def __init__(self, data):
        self.edges = []
        self.data = data

    def neighbors_with_weights(self):
        result = {}
        for edge in self.edges:
            if self != edge.vertex1:
                result[edge.vertex1] = edge.weight

            else:
                result[edge.vertex2] = edge.weight

        return result

    def __str__(self):
        return str(self.data)


class Edge:
    def __init__(self, vertex1, vertex2, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight

    def __str__(self):
        return f"{self.vertex1.data} --({self.weight})-- {self.vertex2.data}"


graph = Graph()

vertex = Vertex(0)
vertex1 = Vertex(1)
vertex2 = Vertex(2)
vertex3 = Vertex(3)
vertex4 = Vertex(4)
vertex5 = Vertex(5)

connect_vertex(vertex, vertex1, 4)
connect_vertex(vertex1, vertex3, 6)
connect_vertex(vertex3, vertex5,2)
connect_vertex(vertex3, vertex2, 7)
connect_vertex(vertex4, vertex3, 10)
connect_vertex(vertex1,vertex5, 4)

graph.add_vertex(vertex)
graph.add_vertex(vertex1)
graph.add_vertex(vertex2)
graph.add_vertex(vertex3)
graph.add_vertex(vertex4)
graph.add_vertex(vertex5)

graph.print_graph()
graph.find_shortest_path(vertex1, vertex3)

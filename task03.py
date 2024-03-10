import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name):
        if name not in self.vertices:
            self.vertices[name] = {}

    def add_edge(self, src, dest, weight):
        if src in self.vertices and dest in self.vertices:
            self.vertices[src][dest] = weight

    def dijkstra(self, start):
        min_heap = [(0, start)]
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0

        while min_heap:
            curr_dist, curr_vertex = heapq.heappop(min_heap)

            if curr_dist > distances[curr_vertex]:
                continue

            for neighbor, weight in self.vertices[curr_vertex].items():
                distance = curr_dist + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))

        return distances

# Приклад використання
graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
graph.add_edge('A', 'B', 6)
graph.add_edge('A', 'D', 1)
graph.add_edge('B', 'D', 2)
graph.add_edge('B', 'E', 2)
graph.add_edge('B', 'C', 5)
graph.add_edge('D', 'E', 1)
graph.add_edge('E', 'C', 5)

start_vertex = 'A'
shortest_distances = graph.dijkstra(start_vertex)
print("Найкоротші відстані від вершини", start_vertex)
for vertex, distance in shortest_distances.items():
    print("До вершини", vertex, ":", distance)
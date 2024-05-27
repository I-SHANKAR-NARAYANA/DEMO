# 7.Dijkstra

import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        dist, node = heapq.heappop(priority_queue)
        print("Extracted from queue", dist, node)
        for neighbor, weight in graph[node].items():
            print(neighbor, weight)
            alt = distances[node] + weight
            if alt < distances[neighbor]:
                print("Updated from ", distances[neighbor], " to ", alt)
                distances[neighbor] = alt
                heapq.heappush(priority_queue, (alt, neighbor))

    return distances


graph = {
    'A': {'B': 100, 'C': 4},
    'B': {'A': 100, 'C': 200},
    'C': {'A': 4, 'B': 200, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
start_vertex = 'B'
shortest_distances = dijkstra(graph, start_vertex)
print("Shortest distances from vertex", start_vertex, ":", shortest_distances)

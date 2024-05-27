# 10. Hamiltonian Cycle

def is_hamiltonian_cycle(graph, v, visited, path, pos):
    if pos == len(graph):
        # Check if the last vertex is connected to the first vertex
        if graph[path[pos - 1]][path[0]]:
            return True
        return False

    for i in range(len(graph)):
        if not visited[i] and graph[v][i]:
            visited[i] = True
            path[pos] = i
            if is_hamiltonian_cycle(graph, i, visited, path, pos + 1):
                return True
            visited[i] = False
            path[pos] = -1  # Reset the path

    return False


graph = [[0, 1, 1, 1, 0],
         [1, 0, 1, 0, 1],
         [1, 1, 0, 1, 1],
         [1, 0, 1, 0, 1],
         [0, 1, 1, 1, 0]]

graph = [
    [0, 1, 1, 1, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 0],
    [1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0]
]

n = len(graph)
visited = [False] * n
path = [-1] * n  # Initialize path with -1

path[0] = 0
visited[0] = True
if is_hamiltonian_cycle(graph, 0, visited, path, 1):
    print("Hamiltonian cycle exists: ", path)
else:
    print("Hamiltonian cycle does not exist")

# 4.Prims

graph = [[0, 2, 0, 6, 0],
         [2, 0, 3, 8, 5],
         [0, 3, 0, 0, 7],
         [6, 8, 0, 0, 9],
         [0, 5, 7, 9, 0]]


def find_min(graph, done):
    min_weight = max(max(graph))
    temp = 0
    for i in range(len(graph)):
        for j in done:
            if graph[j][i] < min_weight and graph[j][i] != 0 and i not in done:
                temp = i
                min_weight = graph[j][i]
    done.append(temp)
    return min_weight


def prims(graph):
    done = [0]
    cost = 0
    while len(done) < len(graph):
        k = find_min(graph, done)
        cost += k
    print(done)
    print(cost)


prims(graph)

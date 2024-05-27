# 8.Articulation points

def dfs(graph, node, parent, ids, low, articulation_points):
    children = 0
    ids[node] = low[node] = dfs.timer
    dfs.timer += 1
    for neighbor in graph[node]:
        if neighbor == parent:
            continue
        if neighbor not in ids:
            children += 1
            dfs(graph, neighbor, node, ids, low, articulation_points)
            low[node] = min(low[node], low[neighbor])
            if parent is not None and low[neighbor] >= ids[node]:
                articulation_points.add(node)
            if parent is None and children > 1:
                articulation_points.add(node)
        else:
            low[node] = min(low[node], ids[neighbor])


# Example usage:
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2, 4],
    4: [3]
}

dfs.timer = 0
articulation_points = set()
dfs(graph, 0, None, {}, {}, articulation_points)
print("Articulation points:", articulation_points)

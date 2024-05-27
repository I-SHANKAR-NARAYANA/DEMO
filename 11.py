# 11.Graph Coloring

def greedy_colouring(graph):
    # Initialize the colouring.
    colouring = {}

    # For each vertex in the graph, assign it the smallest colour that is not already used for any of its neighbours.
    for vertex in graph:
        used_colours = set()
        for neighbour in graph[vertex]:
            if neighbour in colouring:
                used_colours.add(colouring[neighbour])

        colour = 0
        while colour in used_colours:
            colour += 1

        colouring[vertex] = colour

    return colouring


# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colouring = greedy_colouring(graph)
print(colouring)


# The greedy algorithm is a simple and fast algorithm for colouring graphs. However, it does not always find the optimal colouring. For example, the greedy algorithm will always colour the following graph with 3 colours, even though it can be coloured with only 2 colours:

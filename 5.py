# 5.Kruskals

graph = [[0, 2, 0, 6, 0],
         [2, 0, 3, 8, 5],
         [0, 3, 0, 0, 7],
         [6, 8, 0, 0, 9],
         [0, 5, 7, 9, 0]]
done = []


def KST(graph):
    b = []
    for i in range(len(graph)):
        for j in range(len(graph)):
            if (graph[i][j] != 0):
                b.append([graph[i][j], (i+1, j+1)])
    b.sort()
    gra = dict(b)
    kst = list(dict.items(gra))

    dist = 0
    while len(set(done)) < len(graph):
        for i in range(len(kst)):
            if kst[i][1][0] in done and kst[i][1][1] in done:
                pass
            else:
                print(f"edge between {kst[i][1][0]} and {kst[i][1][1]}")
                done.append(kst[i][1][0])
                done.append(kst[i][1][1])
                dist += kst[i][0]

    print(dist)
    # return(dist)


min = KST(graph)

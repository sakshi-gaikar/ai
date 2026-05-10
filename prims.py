graph = {
    'A': [('B', 1), ('D', 4)],
    'B': [('A', 1), ('C', 2)],
    'C': [('B', 2), ('D', 3)],
    'D': [('A', 4), ('C', 3)]
}

visited=set()
visited.add('A')

mst_cost = 0

while len(visited) < len(graph):

    min_edge = (1000, None, None)

    for u in visited:
        for v, w in graph[u]:
            if v not in visited and w < min_edge[0]:
                min_edge = (w, u, v)

    w, u, v = min_edge
    print(u, "-", v, "=", w)

    visited.add(v)
    mst_cost += w

print("Total cost:", mst_cost)
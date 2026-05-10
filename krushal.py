edges = [(2,'B','C'),
         (1,'A','B'),
         (4,'D','A'),
         (3,'C','D')]

edges.sort()

groups = {'A': {'A'}, 'B': {'B'}, 'C': {'C'}, 'D': {'D'}}

cost = 0   # 🔥 added cost variable

for w, u, v in edges:

    # if u and v are in different groups
    if groups[u] != groups[v]:

        print(u, "-", v, "=", w)

        cost += w   # 🔥 add weight to total cost

        # merge groups
        union = groups[u] | groups[v]

        for node in union:
            groups[node] = union

print("Total Cost =", cost)
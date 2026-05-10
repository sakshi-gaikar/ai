graph = {
    'A': [('B',1), ('C',4)],
    'B': [('G',2)],
    'C': [('G',1)],
    'G': []
}

h = {
    'A': 3,
    'B': 1,
    'C': 1,
    'G': 0
}

def astar(start, goal):

    q = [(0, 0, start, [start])]

    while q:

        q.sort()

        f, cost, node, path = q.pop(0)

        if node == goal:
            print("Shortest Path:", path)
            print("Cost:", cost)
            return

        for nextnode, weight in graph[node]:

            new_cost = cost + weight

            new_f = new_cost + h[nextnode]

            q.append((new_f, new_cost, nextnode, path + [nextnode]))

astar('A', 'G')
from collections import deque

graph = {
    'A': ['B','C'],
    'B': ['A','D'],
    'C': ['A','E'],
    'D': ['B'],
    'E': ['C']
}

visited = set()

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for i in graph[node]:
            dfs(i)
            
print("DFS:")
dfs('A')

def bfs(start):
    visited = set()
    q = [start]
    # q = deque([start]) 

    while q:
        node = q.pop(0)
        # node = q.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for i in graph[node]:
                q.append(i)
                
print("\nBFS:")
bfs('A')
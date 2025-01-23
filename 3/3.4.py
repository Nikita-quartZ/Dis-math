def dfs(graph, start, visited):
    visited.add(start)
    print(start)
    for step in graph[start]:
        if step not in visited:
            dfs(graph, step, visited)

num = 20
vertex =  10
edges = []
graph = {}
start = 1

print("Задайте граф: ")

for i in range(num):
    range_from, range_to = map(int, input().split())
    edges.append((range_from, range_to))

for i in range(1, vertex + 1):
    graph[i] = []

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

print("Алгоритм dfs: ")
dfs(graph, start, visited=set())


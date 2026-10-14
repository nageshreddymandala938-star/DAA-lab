
import heapq

n = int(input("Enter number of vertices: "))

graph = [[] for _ in range(n)]

m = int(input("Enter number of edges: "))

print("Enter edges (u v weight):")
for _ in range(m):
    u, v, w = map(int, input().split())

    graph[u].append((w, v))
    graph[v].append((w, u))

visited = [False] * n
min_heap = [(0, 0)]  # (weight, vertex)

total_cost = 0
edges = 0

print("\nEdges in Minimum Spanning Tree:")

while min_heap and edges < n - 1:
    weight, u = heapq.heappop(min_heap)

    if visited[u]:
        continue

    visited[u] = True
    total_cost += weight

    if weight != 0:
        print("Vertex", u, "with edge weight", weight)
        edges += 1

    for w, v in graph[u]:
        if not visited[v]:
            heapq.heappush(min_heap, (w, v))

if edges == n - 1:
    print("Minimum Cost =", total_cost)
else:
    print("Graph is disconnected; MST does not exist.")

from collections import deque
import sys

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for i in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

cnt = 0

for i in range(1, N+1):
    if not visited[i]:
        bfs(graph, i, visited)
        cnt += 1
print(cnt)

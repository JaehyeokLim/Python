from dis import dis
import sys
from collections import deque

def bfs(x):
  queue = deque([x])
  while queue:
      now = queue.popleft()
      for next in graph[now]:
          if distance[next] == -1:
              distance[next] = distance[now] + 1
              queue.append(next)


N, M, K, X = map(int, sys.stdin.readline().split())
graph= [[] * M for _ in range(N + 1)]
distance = [-1] * (N + 1)
distance[X] = 0
result = []

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

bfs(X)

for i in range(1, N + 1):
    if distance[i] == K:
        result.append(i)

result.sort()

if len(result) == 0:
    print(-1)
else: 
    for i in range(len(result)):
        print(result[i])
    
print(distance)
    




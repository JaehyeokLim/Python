import sys
import heapq

N, D = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(D+1)]

for i in range(D):
    graph[i].append((i+1, 1))

for i in range(N):
    start, end, length = map(int, sys.stdin.readline().split())
    if end > D: continue
    graph[start].append((end, length))

INF = 10e6
distance = [INF]*(D+1)
distance[0], q = 0, []

heapq.heappush(q, (0, 0))

while q:
    d, now = heapq.heappop(q) 
    if distance[now] < d: continue 

    for x in graph[now]: 
        cost = d + x[1] 

        if distance[x[0]] > cost:
            distance[x[0]] = cost
            heapq.heappush(q, (cost, x[0]))

print(distance[D])
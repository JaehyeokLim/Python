import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
    # 함수 실행마다 최단거리 리스트 초기화 
    distance = [INF] * (n + 1)
    q = []
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # q가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

# 다익스트라 알고리즘을 수행
# 1 - > v1 -> v2 - > n(마지막 정점) 이들을 합쳐서 최소값 출력

distance_one = dijkstra(1)
distance_v1 = dijkstra(v1)
distance_v2 = dijkstra(v2)
sol_v1 = distance_one[v1] + distance_v1[v2]  + distance_v2[n]
sol_v2 = distance_one[v2] + distance_v2[v1]  + distance_v1[n]

final_sol = min(sol_v1, sol_v2)

if final_sol < INF:
    print(final_sol)
else:
    print(-1)
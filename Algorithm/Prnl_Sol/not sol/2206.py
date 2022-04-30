import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    dist = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    skill = 1
    q = deque()
    q.append([0, 0])
    visited[0][0] = True
    dist[0][0] = 1
    while q:
        x, y = q.popleft()
        if x == N-1 and y == M-1:
            return dist[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if world[nx][ny] == 0 and visited[nx][ny] == False:
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                q.append([nx, ny])
            if world[nx][ny] == 1 and skill == 1:
                skill -= 1
                world[nx][ny] = 0
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                q.append([nx, ny])
            if world[nx][ny] == 1 and skill == 0:
                skill += 1
                q.append([x, y])
    return -1



N, M = map(int, sys.stdin.readline().split())

world = []

for _ in range(N):
    world.append(list(map(int, sys.stdin.readline().rstrip())))

# while True:
#     if bfs() == None:
#         continue
#     else:
#         result.append(answer)
#         break
# print(result)
#     print(dist[M][N])
print(bfs())


# for i in range(N):
#     print(world[i])

# for i in range(N):
#     print(dist[i])
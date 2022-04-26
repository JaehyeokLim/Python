import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < M and 0 <= ny < N and tomato_farm[nx][ny] == 0:
                tomato_farm[nx][ny] = tomato_farm[x][y] + 1
                queue.append([nx, ny])

N, M = map(int, sys.stdin.readline().split())
tomato_farm = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
queue = deque([])
result = 0

# for _ in range(M):
#     tomato_farm.append(list(map(int, sys.stdin.readline().split())))
                
for i in range(M):
    for j in range(N):
        if tomato_farm[i][j] == 1:
            queue.append([i, j])
            break
            
bfs()

for i in tomato_farm:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result, max(i))
print(result - 1)


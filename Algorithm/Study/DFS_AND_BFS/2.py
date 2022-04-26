import sys
from collections import deque
sys.setrecursionlimit(100000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    return maze[N-1][M-1]

N, M = map(int, sys.stdin.readline().split())

maze = [] 

visited = [[False] * M for _ in range(N)]

for i in range(N):
    maze.append(list(map(int, input())))

for i in range(len(maze)):
    print(maze[i])
print(bfs(0,0))
import sys
from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

N, M = map(int, sys.stdin.readline().split())
ocean = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(M)]
queue = deque([])

for i in range(N):
    for j in range(M):
        if ocean[i][j] == 9:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if x <= -1 or x >= N or y <= -1 or y >= M:
                continue
                
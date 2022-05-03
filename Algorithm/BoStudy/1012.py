import sys
from collections import deque
sys.setrecursionlimit(10000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    while bq:
        x, y = bq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < N) and (0 <= ny < M):
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    bq.append([nx, ny])
                    

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    bq = deque()

    for _ in range(T):
        M, N, B = map(int, sys.stdin.readline().split())
        graph = [[0] * M for _ in range(N)]
        cnt = 0
        for _ in range(B):
            m, n = map(int, sys.stdin.readline().split())
            graph[n][m] = 1
        for i in range(N):
            for j in range(M):
                if graph[i][j] > 0:
                    graph[i][j] = 0
                    bq.append([i, j])
                    bfs()
                    cnt += 1
        print(cnt)

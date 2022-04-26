import sys
sys.setrecursionlimit(10000)
def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < N) and (0 <= ny < M):
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                dfs(nx, ny)
 
T = int(sys.stdin.readline())
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
                dfs(i, j)
                cnt +=1
    print(cnt)
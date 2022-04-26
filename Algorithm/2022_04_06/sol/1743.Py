import sys
sys.setrecursionlimit(100000)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y, count):
    list[x][y] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 1 or nx > n or ny < 1 or ny > m or list[nx][ny] != 1:
            continue
        count = max(count, dfs(nx, ny, count + 1))
    return count

n, m, k = map(int, sys.stdin.readline().split())

list = [[0] * (m + 1) for _ in range(n + 1)]

cnt = []

for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    list[r][c] = 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if list[i][j] == 1:
            cnt.append(dfs(i, j, 1))

print(max(cnt))
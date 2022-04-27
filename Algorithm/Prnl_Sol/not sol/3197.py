import sys
from collections import deque
sys.setrecursionlimit(100000000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global distance_dfs
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= H or ny < 0 or ny >= W:
            continue
        if backjo[nx][ny] == 'X':
            backjo[nx][ny] = '.'
            distance_dfs[nx][ny] = True

def bfs():
    global distance_bfs
    global L
    limit = 0
    distance_bfs[L[0]][L[1]] = True
    while q:
        x, y = q.popleft()
        if limit == 4:
            return 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if backjo[nx][ny] == 'X':
                limit += 1
                continue
            if backjo[nx][ny] == '.' and distance_bfs == False:
                limit = 0
                distance_bfs[nx][ny] = True
                q.append([nx, ny])
            if backjo[nx][ny] == backjo[L[2]][L[3]]:
                return 1
            limit += 1
    return 0

backjo = []
L = []
count = 0
q = deque([])

H, W = map(int, sys.stdin.readline().split())

for i in range(H):
    backjo.append(list(map(str, sys.stdin.readline().rstrip())))

for i in range(H):
    for j in range(W):
        if backjo[i][j] == 'L':
            L.append(i)
            L.append(j)
q.append([L[0], L[1]])

while True:
    distance_dfs = [[False] * W for i in range(H)]
    distance_bfs = [[False] * W for i in range(H)]

    for i in range(H):
        for j in range(W):
            if backjo[i][j] == '.' and distance_dfs[i][j] == False:
                dfs(i, j)
    count += 1
    # # print("{}주차".format(count+1))
    # # for i in range(H):
    # #     print(backjo[i])

    # if count == 2:
    #     break

    if bfs() == 1:
        print(count)
        break
    else:
        continue

                

    
        
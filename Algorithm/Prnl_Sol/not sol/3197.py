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

def bfs(x, y):
    q = deque([(x, y)])
    distance_bfs[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if backjo[nx][ny] == 'X':
                continue
            if backjo[nx][ny] == '.' and distance_bfs[nx][ny] == True:
                continue
            if backjo[nx][ny] == backjo[x2][y2]:
                return 1
            if backjo[nx][ny] == '.' and distance_bfs[nx][ny] == False:
                q.append((nx, ny))
                distance_bfs[nx][ny] = True
    return 0

backjo = []
L = []
count = 0

H, W = map(int, sys.stdin.readline().split())

for i in range(H):
    backjo.append(list(map(str, sys.stdin.readline().rstrip())))

for i in range(H):
    for j in range(W):
        if backjo[i][j] == 'L':
            L.append((i, j))

(x1, y1), (x2, y2) = L

while True:
    distance_dfs = [[False] * H for _ in range(W)]
    distance_bfs = [[False] * H for _ in range(W)]

    if bfs(x1, y1) == 1:
        print(count)
        break
    else:
        for i in range(H):
            for j in range(W):
                if backjo[i][j] == '.' and distance_dfs[i][j] == False:
                    dfs(i, j)
    count += 1
    # print("{}주차".format(count+1))
    # for i in range(H):
    #     print(backjo[i])

    # if count == 3:
    #     break

 

                

    
        
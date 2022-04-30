import sys
from collections import deque
sys.setrecursionlimit(100000000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global visited_dfs
    visited_dfs[x][y] == True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= H or ny < 0 or ny >= W:
            continue
        if backjo[nx][ny] == 'X':
            backjo[nx][ny] = '.'
            visited_dfs[nx][ny] = True
            dfs(nx, ny)
        if backjo[nx][nx] == '.' and visited_dfs[nx][ny] == True:
            continue

# def bfs(x, y):
#     q = deque()
#     q.append([x, y])
#     visited_bfs[x][y] = True
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx == x2 and ny == y2:
#                 return 1
#             if nx < 0 or nx >= H or ny < 0 or ny >= W:
#                 continue
#             if backjo[nx][ny] == 'X':
#                 continue
#             if backjo[nx][ny] == '.' and visited_bfs[nx][ny] == True:
#                 continue
#             if backjo[nx][ny] == '.' and visited_bfs[nx][ny] == False:
#                 q.append([nx, ny])
#                 visited_bfs[nx][ny] = True
#     return 0

backjo, L = [], []

H, W = map(int, sys.stdin.readline().split())

for i in range(H):
    backjo.append(list(map(str, sys.stdin.readline().rstrip())))

for i in range(H):
    for j in range(W):
        if backjo[i][j] == 'L':
            L.append((i, j))

(x1, y1), (x2, y2) = L

count = 0
# print(x1, y1, x2, y2)

while True:
    visited_dfs = [[False] * W for _ in range(H)]
    visited_bfs = [[False] * W for _ in range(H)]

    # if bfs(x1, y1) == 1:
    #     print(count)
    #     break
    # else:
    #     for i in range(H):
    #         for j in range(W):
    #             if backjo[i][j] == '.' and visited_dfs[i][j] == False:
    #                 dfs(i, j)

    for i in range(H):
        for j in range(W):
            if backjo[i][j] == '.' and visited_dfs[i][j] == False:
                dfs(i, j)
                
    count += 1

    # if bfs(x1, y1) == 1:
    #     print(count)
    #     break
    print("{}주차".format(count))
    for i in range(H):
        print(backjo[i])

    if count == 3:
        break

 

                

    
        
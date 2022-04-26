import sys
from collections import deque
sys.setrecursionlimit(100000000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def change():
    global dfs_cnt
    if dfs_cnt + 2 not in dfs_cnt_list:
        dfs_cnt_list.append(dfs_cnt + 2)
    return dfs_cnt + 2

def dfs(x, y):
    world_map[x][y] = change()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <= -1 or nx >= N or ny <= -1 or ny >= N or world_map[nx][ny] != 1:
            continue
        dfs(nx, ny)

def bfs(z):
    global answer
    dist = [[-1] * N for _ in range(N)] # 거리가 저장될 배열
    q = deque()

    for i in range(N):
        for j in range(N):
            if world_map[i][j] == z:
                q.append([i, j])
                dist[i][j] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 갈 수 없는 곳이면 continue
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            # 다른 땅을 만나면 기존 답과 비교하여 짧은 거리 선택
            if world_map[nx][ny] > 0 and world_map[nx][ny] != z:
                answer = min(answer, dist[x][y])
                return
            # 바다를 만나면 dist를 1씩 늘린다.
            if world_map[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append([nx, ny])

                
def program(x):
    for i in range(N):
        for j in range(N):
            if world_map[i][j] == x and x not in check_bfs:
                check_bfs.append(x)
                result.append((bfs(x)))

N = int(input())
world_map, result, dfs_cnt_list, check_bfs, dfs_cnt = [], [], [], [], 0
answer = sys.maxsize

for _ in range(N):
    world_map.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(N):
        if world_map[i][j] == 1:
            dfs(i, j)
            dfs_cnt += 1   

for i in range(len(dfs_cnt_list)):
    program(dfs_cnt_list[i]) 
    
print(answer)


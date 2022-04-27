import sys
from collections import deque
sys.setrecursionlimit(100000000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def lazer():
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= H or ny < 0 or ny >= W or world[nx][ny] == '*' or world[nx][ny] == '|' and world[nx][ny] == '-':
                continue
            if world[nx][ny] == '.' and nx == x and (ny == y -1 or ny == y + 1):
                world[nx][ny] = '|'
                queue.append([nx, ny])
            if world[nx][ny] == '.' and ny == y and (nx == x -1 or nx == x + 1):
                world[nx][ny] = '-'
                queue.append([nx, ny])



            


world = []
queue = deque([])
W, H = map(int, sys.stdin.readline().split())

for _ in range(H):
    world.append(list(map(str, sys.stdin.readline().rstrip())))

for i in range(H):
    for j in range(W):
        if world[i][j] == 'C':
            queue.append([i, j])
            break

lazer()
for i in range(H):
    print(world[i])
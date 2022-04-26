import sys
from collections import deque
sys.setrecursionlimit(100000000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def lazer(x, y):
    count = 1
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = x + dy[i]
            if nx < 0 or nx >= H or ny < 0 or ny >= W or world[nx][ny] == '*' or world[nx][ny] == '|' and world[nx][ny] == '-':
                continue
            if world[nx][ny] == '.' and nx == x:
                world[nx][ny] = '|'
            if world[nx][ny] == '.' and ny == y:
                world[nx][ny] = '-'



            


world = []

W, H = map(int, sys.stdin.readline().split())

for _ in range(H):
    world.append(list(map(str, sys.stdin.readline().rstrip())))

for i in range(H):
    for j in range(W):
        if world[i][j] == 'C':
            lazer(i, j)
            break

for i in range(H):
    print(world[i])
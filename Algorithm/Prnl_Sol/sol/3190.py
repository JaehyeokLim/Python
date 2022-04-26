import sys
from collections import deque
sys.setrecursionlimit(100000)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def cng(d, times_key):
    if times_key == "L":
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d

def dummys():
    direction = 1
    time = 1
    x, y = 0, 0
    dummy[x][y] = 2
    visited = deque([[x, y]])
    while True:
        x, y = x + dx[direction], y + dy[direction]
        if 0 <= y < N and 0 <= x < N and dummy[x][y] != 2:
            if not dummy[x][y] == 1:
                temp_x, temp_y = visited.popleft()
                dummy[temp_x][temp_y] = 0  # 꼬리 제거
            dummy[x][y] = 2
            visited.append([x, y])
            if time in times.keys():
                direction = cng(direction, times[time])
            time += 1
        else:
            return time
            

N = int(input())
dummy = [[0] * N for _ in range(N + 1)]
K = int(input())

for _ in range(K):
    kn, km = map(int, input().split())
    dummy[kn - 1][km - 1] = 1

times = {}
L = int(input())

for _ in range(L):
    X, C = input().split()
    times[int(X)] = C
    
print(dummys())





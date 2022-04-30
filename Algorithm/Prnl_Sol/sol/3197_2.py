import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def ice_melt():
    while iceq:
        x, y = iceq.popleft()
        if lake[x][y] == 'X':
            lake[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if visited_melt[nx][ny] == False:
                    if lake[nx][ny] == 'X':
                        iceq_temp.append([nx, ny])
                    else:
                        iceq.append([nx, ny])
                    visited_melt[nx][ny] = True

def swan_mov():
    while swanq:
        x, y = swanq.popleft()
        if x == x2 and y == y2:
            return 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if visited[nx][ny] == False:
                    if lake[nx][ny] == '.':
                        swanq.append([nx, ny])
                    else:
                        swanq_temp.append([nx, ny])
                    visited[nx][ny] = True
    return 0

if __name__ == "__main__":

    R, C = map(int, sys.stdin.readline().split())
    lake, swan = [], []
    swanq, swanq_temp, iceq, iceq_temp, count = deque(), deque(), deque(), deque(), 0
    visited = [[False] * C for _ in range(R)]
    visited_melt = [[False] * C for _ in range(R)]

    for i in range(R):
        row = list(sys.stdin.readline().strip())
        lake.append(row)
        for j, k in enumerate(row): ## enumerate함수는 인터넷에서 찾음.
            if lake[i][j] == 'L':
                swan.extend([i, j])
                iceq.append([i, j])
            elif lake[i][j] == '.':
                visited_melt[i][j] = True
                iceq.append([i, j])

    x1, y1, x2, y2 = swan
    swanq.append([x1, y1])

    lake[x1][y1], lake[x2][y2], visited[x1][y1] = '.', '.', True

    while True: 
        ice_melt()
        if swan_mov():
            print(count)
            break
        iceq, swanq = iceq_temp, swanq_temp
        iceq_temp, swanq_temp = deque(), deque()
        count += 1
              


    



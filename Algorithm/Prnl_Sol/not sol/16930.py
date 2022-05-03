import sys
from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def run():
    time = 0
    K_temp = K
    K_temp -= 1
    while rq:
        x, y = rq.popleft()
        if x == (x2 - 1) and y == (y2 - 1):
            return time
        if K_temp == 0:
            time += 1
            K_temp = K
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if gym[nx][ny] == '.' and visited[nx][ny] == 0:
                    K_temp -= 1
                    rq.append([nx, ny])
                    visited[nx][ny] = 1
                    while True:
                        rx, ry = nx + dx[i], ny + dy[i]
                        if K_temp == 0:
                            time += 1
                            K_temp = K
                        if not (0 <= rx < N and 0 <= ry < M):
                            break
                        if rx == (x2 - 1) and ry == (y2 - 1):
                            break
                        if gym[rx][ry] == '#':
                            break
                        if gym[rx][ry] == '.' and visited[rx][ry] == 0:
                            K_temp -= 1
                            visited[rx][ry] = 1
                            nx, ny = rx, ry
                    rq.append([nx, ny])
    return -1

if __name__ == "__main__":
    N, M, K = map(int, sys.stdin.readline().split())
    gym = [list(map(str, sys.stdin.readline().rstrip())) for i in range(N)]
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    visited = [[0] * M for i in range(N)]
    visited[x1-1][y1-1] = 1

    rq = deque()
    rq.append([x1-1, y1-1])

    print(run())
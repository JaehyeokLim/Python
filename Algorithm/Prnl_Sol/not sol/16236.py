from multiprocessing import shared_memory
import sys
from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def shark_mov():
    shark_size = 2
    shark_size_up = shark_size
    time = 0
    while sq:
        x, y = sq.popleft()
        if shark_size_up == 0:
            shark_size += 1
            shark_size_up = shark_size
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if ocean[nx][ny] == 0 or ocean[nx][ny] == shark_size:
                    sq.append([nx, ny])
                    time += 1
                if ocean[nx][ny] > shark_size:
                    ocean[nx][ny] = 0
                    shark_size_up -= 1
                    sq.append([nx, ny])
                    time += 1
                if ocean[nx][ny] < shark_size:
                    continue
    return time


                
if __name__ == "__main__":
    N= int(sys.stdin.readline())
    ocean = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    sq = deque([])

    for i in range(N):
        for j in range(N):
            if ocean[i][j] == 9:
                sq.append([i, j])
                break

    print(shark_mov())

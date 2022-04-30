import sys
from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def shark_mov():
    d
if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    ocean = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(M)]
    visited = [[False] * N for _ in range(M)]
    sq = deque([])

    for i in range(N):
        for j in range(M):
            if ocean[i][j] == 9:
                sq.append([i, j])
                break

    shark_mov()

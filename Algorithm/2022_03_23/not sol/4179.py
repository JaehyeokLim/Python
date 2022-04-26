from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R, C = map(int, input().split())

def bfs(x, y, f_x, f_y):
    queue = deque()
    queue.append((x, y))
                
    fire = deque()
    fire.append((f_x, f_y))
    
    while queue and fire:
        x, y = queue.popleft()
        f_x, f_y = fire.popleft()
        # maze_map[x][y] = '.'
        # maze_map[f_x][f_y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nf_x, nf_y = f_x + dx[i], f_y + dy[i]
            if nx < 0 or ny < 0 or nx >= R or ny > C or nf_x < 0 or nf_y < 0 or nf_x >= R or nf_y >=C:
                continue
            if maze_map[nx][ny] == '#' or maze_map[nf_x][nf_y] == '#':
                continue
            if maze_map[nx][ny] == '.':
                maze_map[nx][ny] = 'J'
                queue.append((nx, ny))
            if maze_map[nf_x][nf_y] == '.':
                maze_map[nf_x][nf_y] = 'F'
                queue.append((nf_x, nf_y))
            if maze_map[nx][ny] == 'F' or maze_map[nf_x][nf_y] == 'J' or maze_map[nf_x][nf_y] == maze_map[3][2]:
                return print("IMPOSSIBLE")
            if maze_map[nx][ny] == maze_map[3][2]:
                return print("END!!")


maze_map = []
x1, y1 = 0, 0
x2, y2 = 0, 0

for _ in range(R):
    maze_map.append(list(map(str, input().rstrip())))

for i in range(R):
        for j in range(C):
            if maze_map[i][j] == 'F':
                x2 += i
                y2 += j

for i in range(R):
    for j in range(C):
        if maze_map[i][j] == 'J':
            x1 += i
            y1 += j

bfs(x1, y1, x2, y2)

for i in range(len(maze_map)):
    print(maze_map[i])


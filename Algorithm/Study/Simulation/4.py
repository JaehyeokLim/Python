import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3    

N, M = map(int, input().split())

ch_x, ch_y, direction = map(int, input().split())

game_map = []

for i in range(N):
    game_map.append(list(map(int, sys.stdin.readline().split())))

game_map[ch_x][ch_y] = 1
count = 1
turn_time = 0

while True:
    turn_left()
    nx = ch_x + dx[direction]
    ny = ch_y + dy[direction]

    if game_map[nx][ny] == 0:
        game_map[nx][ny] = 1
        ch_x = nx
        ch_y = ny
        count += 1
        turn_time = 0
    else:
        turn_time += 1
    
    if turn_time == 4:
        nx = ch_x + dx[direction]
        ny = ch_y + dy[direction]
        if game_map[nx][ny] == 0:
            ch_x = nx
            ch_y = ny
            turn_time = 0
        else:
            break
print(count)



import sys
sys.setrecursionlimit(100000000)

dx = [1, 1, -1, -1, 1, -1, 0, 0]
dy = [0, 1, 0, 1, -1, -1, 1, -1]

def changed():
    global dfs_cnt_list, dfs_cnt
    if dfs_cnt + 2 not in dfs_cnt_list:
        dfs_cnt_list.append(dfs_cnt + 2)
    return dfs_cnt + 2

def dfs(x, y):
    matrix[x][y] = changed()
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <= -1 or nx >= h or ny <= -1 or ny >= w:
            continue
        if matrix[nx][ny] == 1:
            dfs(nx, ny)
        # if matrix[nx][ny] == 0:
        #     for i in range(4):
        #         nnx = nx + dy[i] + ddx[i]
        #         nny = ny + dy[i] + ddy[i]
        #         if nnx <= -1 or nnx >= h or nny <= -1 or nny >= w or matrix[nnx][nny] != 1:
        #             continue
        #         dfs(nnx, nny) 
        #     break
            

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    else:
        matrix = [list(map(int, input().split())) for _ in range(h)]
        dfs_cnt, dfs_cnt_list = 0, []

        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 1:
                    dfs(i, j)
                    dfs_cnt += 1
        
        print(dfs_cnt)
                 

    # for i in range(len(matrix)):
    #     print(matrix[i])

    # for i in range(len(dfs_cnt_list)):
    #     print(dfs_cnt_list[i])
    
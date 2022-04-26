import sys
sys.setrecursionlimit(10**6)

m, n = map(int, input().split())

graph = []
for _ in range(m):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 2
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

for i in range(n):
    if graph[0][i] == 0:
        dfs(0, i)

if 2 in graph[m-1]:
    print("YES")
else:
    print("NO")
for i in range(len(graph)):
    print(graph[i])

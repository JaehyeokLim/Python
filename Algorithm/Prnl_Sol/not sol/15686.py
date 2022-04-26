import sys

N = int(input())
graph = []

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

for i in range(len(graph)):
    print(graph[i])
    

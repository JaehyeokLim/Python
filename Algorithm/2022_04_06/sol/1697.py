import sys 
from collections import deque 

def bfs():
    q = deque() 
    q.append(N) 
    while q: 
        X = q.popleft() 
        if X == K: 
            print(distance[X]) 
            break 
        for j in (X - 1, X + 1, X * 2): 
            if 0 <= j <= maxnum and not distance[j]: 
                distance[j] = distance[X] +1 
                q.append(j) 
                

input = sys.stdin.readline() 
N, K = map(int,input.split()) 
# maxnum = int(10e6)
maxnum = int(10e4)
distance = [0] * (maxnum+1) 

bfs()


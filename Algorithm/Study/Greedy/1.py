import sys

N, M, K = map(int, sys.stdin.readline().split())

list = list(map(int, input().split()))

print(list)

list.sort()

result = 0
o = 1
for i in range(M):
    if i != K * o:
        for j in range(K):
            result += list[0]
    else:
        result += list[1]
    
    
print(result)
    
    

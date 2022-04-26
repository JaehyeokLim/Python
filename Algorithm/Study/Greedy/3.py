import sys

N, K = map(int, sys.stdin.readline().split())

count = 0

while N >= K:
    if N % K == 0:
        N //= K
        count += 1
    elif N % K == 1:
        N -= 1
        count += 1
    elif N == 1:
        break
print(count)
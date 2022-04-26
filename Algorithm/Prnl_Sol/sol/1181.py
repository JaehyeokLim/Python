import sys

N = int(sys.stdin.readline())
lst = []

for i in range(N):
    lst.append(sys.stdin.readline().strip())

setl = set(lst)
lst = list(setl)

lst.sort()
lst.sort(key = len)

for i in range(len(lst)):
    print(lst[i])


    
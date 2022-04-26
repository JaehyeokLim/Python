# import sys

# N = int(input())

# list =[]

# for i in range(N):
#     p, d = map(int, sys.stdin.readline().split())
#     list.append((p, d))

# list.sort(reverse= True)

# money = 0
# time = 1
# temp = []
# temp.append(0)
# print(list)
# while len(list) > 0:
#     if list[0][1] in temp:
#         if list[0][1] >= time:
#             money += list[0][0]
#             time += 1
#         del list[0]
#     else:
#         if list[0][1] >= time:
#             money += list[0][0]
#             temp.append(list[0][1])
#             time += 1
#         else:
#             money += list[0][0]
#         del list[0]
        
# print(money)

n = int(input())
if n == 0:
    print(0)
    exit()

arr = []

for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a,b))

arr.sort(reverse = True)

max_day = max(arr[i][1] for i in range(len(arr))) + 1
money = 0
visit = [0] * max_day

for val, day in arr: 
    for i in range(day, 0, -1): 
        if not visit[i]: 
            visit[i] = 1 
            money += val 
            break
print(money)


# from pickle import HIGHEST_PROTOCOL
# import sys

# N, D  = map(int, input().split())

# highway = [[False] for _ in range(D + 1)]

# for i in range(N):
#     s, e, l = map(int, input().split())
#     highway[s].append([e, l])

# now, cost, maxn = 0, 0

# print(len(highway[0]))
# while now != D:
#     for now in range(D+1):
#         if highway[now] == False:
#             continue
#         else:
#             if len(highway[now]) == 2:
#                 cost += highway[now][0][1]
#                 now = highway[now][0][0]
#             else:
#                 for i in range(len(highway[i])):
#                     maxn = min(highway[now][i][1], highway[now][i+1][1])
#                 cost += maxn
#                 now = h


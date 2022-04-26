# import sys
# import math

# N, M = map(int, sys.stdin.readline().split())
# num = M
# # def prime(x):
# #     if x < 2:
# #         return False
# #     for i in range(2, x):
# #         if x % i == 0:
# #             return False
# #     return True


# # for N in range(M+1):
# #     if prime(N) == True:
# #         print(N)

# array = [True for _ in range(num + 1)]

# for i in range(2, int(math.sqrt(num)) + 1):
#     if array[i] == True:
#         j = 2
#         while i * j <= num:
#             array[i * j] = False
#             j += 1

# for i in range(N, M + 1):
#     if array[i]:
#         print(i)

M, N = map(int, input().split())

N += 1
list = [True] * N

for i in range(2, int(N ** 0.5) +1):
    if list[i]:
        for j in range(2 * i, N, i):
            list[j] = False
for i in range(M, N):
    if i > 1:
        if list[i]:
            print(i)

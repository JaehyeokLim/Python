import sys

N, M = map(int, sys.stdin.readline().split())

deck = []
max_in_min = []

for i in range(N):
    deck.append(list(map(int, input().split())))

max_in_min.append(max(min(deck[0]), min(deck[1]), min(deck[2])))

print(max_in_min[0])
# result = min(max_in_min)
# print(result)
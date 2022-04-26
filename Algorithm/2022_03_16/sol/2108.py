import sys
from collections import Counter

n = int(sys.stdin.readline())
box = []

for _ in range(n):
    box.append(int(int(sys.stdin.readline()))) # 사용자 입력 n개만큼 입력 받기.

print(round(sum(box)/n))

box.sort()
print(box[int((n-1)/2)])

box_t = Counter(box).most_common() # 몰랐던 것.

if len(box_t) > 1:
    if box_t[0][1] == box_t[1][1]:
        print(box_t[1][0])
    else:
        print(box_t[0][0])
else:
    print(box_t[0][0])

print(box[n-1] - box[0])






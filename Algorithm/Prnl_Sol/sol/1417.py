import sys
from termios import NL1

T = int(sys.stdin.readline())
num = []
count = 0

for i in range(T):
    N = int(sys.stdin.readline())
    num.append(N)

while(max(num) != num[0]):
        num[num.index(max(num))] -= 1
        num[0] += 1
        count += 1

if num.count(max(num)) >= 2:
    print(count + 1)
else:
    print(count)
    


import sys
from collections import Counter

N = []
R = []

# N = list(map(int, input().split()))
N = list(map(int, map(str, input())))

print("입력된 데이터 : ", end = '')
for i in range(len(N)):
    print(N[i], end = '')

print()

if (N[0] + N[1] + N[3] + N[4] + N[6]) % 2 == 0:
    R.append(0)
else:
    R.append(1)
    
if (N[0] + N[2] + N[3] + N[5] + N[6]) % 2 == 0:
    R.append(0)
else:
    R.append(1)    

if (N[1] + N[2] + N[3] + N[7]) % 2 == 0:
    R.append(0)
else:
    R.append(1)

if (N[4] + N[5] + N[6] + N[7]) % 2 == 0:
    R.append(0)
else:
    R.append(1)

N.insert(0, R[0])
N.insert(1, R[1])
N.insert(3, R[2])
N.insert(7, R[3])

print("해밍코드      : ", end = '')
for i in range(len(N)):
    print(N[i], end = '')

print()
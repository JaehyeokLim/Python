import sys
import math

N = []
H = []
n = 0

N = list(map(int, map(str, input())))

if (N[0] + N[2] + N[4] + N[6] + N[8] + N[10]) % 2 == 0:
    H.append(0)
else:
    H.append(1)
    
if (N[1] + N[2] + N[5] + N[6] + N[9] + N[10]) % 2 == 0:
    H.append(0)
else:
    H.append(1)    

if (N[3] + N[4] + N[5] + N[6] + N[11]) % 2 == 0:
    H.append(0)
else:
    H.append(1)

if (N[7] + N[8] + N[9] + N[10] + N[11]) % 2 == 0:
    H.append(0)
else:
    H.append(1)

for i in range(len(H)):
    if H[i] == 1:
        n += int((math.pow(2, i)))

print("기존 해밍코드   : ", end = '')
for i in range(len(N)):
    print(N[i], end = '')
print()

del N[n-1]
N.insert(n-1, 0)

if n == 0:
    print("No Error!")
else:
    print("{}번째 비트에 에러가 발생!".format(n))
    print("수정된 해밍코드 : ", end = '')
    for i in range(len(N)):
        print(N[i], end = '')
print()
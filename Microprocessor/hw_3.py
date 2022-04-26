N = list(map(str, map(str, input())))
crr = []

print("입력된 비트열 : ", end = '')
for i in range(len(N)):
    print(N[i], end = '')
print()

for i in range(3):
    crr.append('0')

for i in range(6):
    if N[i] == crr[0]:
        bit = '0'
    else:
        bit = '1'
    if bit == crr[1]:
        crr[0] = '0'
    else:
        crr[0] = '1'
    crr[1] = crr[2]
    crr[2] = bit
    for i in range(len(crr)):
        print(crr[i], end = '')
    print()

print("FCS : ", end = '')
for i in range(len(crr)):   
    print(crr[i], end = '')
print()

bi = [0, 1, 1]

n = int(input())

for i in range(3, 91):
  bi.append(bi[i - 2] + bi[i - 1])

print(bi[n])
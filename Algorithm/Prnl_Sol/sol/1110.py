from curses.ascii import NL


N = int(input()) # 26
num = N
count = 0

while True:
    a = num // 10 # 2
    b = num % 10  # 6
    c = (a + b) % 10 # 2 + 6 % 10 = 8
    num = (b * 10) + c
    count += 1

    if num == N:
        break

print(count)




N = int(input())
M = int(input())

sticker = [list(map(int, input().split())) for _ in range(N)]
result = 0
indexB = []

for i in range(N):
    maxi = max(sticker[i])
    result += maxi
    indexB.append(sticker.index(max(sticker[i])))
    sticker[i][indexB] = 0
    if indexB[i] == N - 1 and not 0:
        sticker[i][indexB[i] + 1] = 0
        sticker[i+1][indexB[i]] = 0
    if indexB[i] == N - 1 and not N: 
        sticker[i][indexB[i] - 1] = 0
        sticker[i+1][indexB[i]] = 0


print(sticker)
    
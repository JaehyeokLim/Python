import sys

def aaa():
    # result = 0
    # temp = [-1] * N
    # for i in range(len(food)):
    #     if food[i] == max(food) and temp[i] == -1:
    #         result += food[i]
    #         temp[i] = food[i]
    #         food[i] = -1
    # return result
    for i in range(len(food)):
        for j in range(len(food)):
            if food[i] < food[j]:
                i = j
                

N = int(input())

food = (list(map(int, sys.stdin.readline().split())))

print(aaa())


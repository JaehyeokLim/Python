import sys
N = int(input())
out = []
time = 0
act_time = 0
sub_time = 0
temp = []
total_m = 0

for i in range(N):
    T, P = map(int, sys.stdin.readline().split())   
    out.append([T,P])

for i in range(len(out)):
     time = i + 1
     act_time += time + out[0][0]
     sub_time = time
     while True:
        if sub_time < act_time:
            if out[sub_time - 1][1] >= out[sub_time][1]:
                total_m += out[sub_time-1][1]
                False
            else:
                sub_time += 1
                True
        False        
print(total_m)  

# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200
import sys

T = int(input())
grade = []

for i in range(T):
    count = 1
    grade.clear()

    N = int(input())

    for j in range(N):
        report, interview = map(int, sys.stdin.readline().split())
        grade.append([report, interview])
    grade.sort()
    elite = grade[0][1]

    for k in range(N):
         if elite > grade[k][1]:
            count += 1
            elite = grade[k][1]
    print(count)
import sys
sys.setrecursionlimit(100000)


def fibonacci(n):
    global count_z 
    global count_o
    if n in fib:
        if n == 0:
            count_z += 1
            return fib[0]
        if n == 1:
            count_o += 1
            return fib[1]
        return fib[n]

    if n == 0 :
        fib[0] = 0
        count_z += 1
        return 0
    elif n == 1:
        fib[1] = 1
        count_o += 1
        return 1
    else:
        fib[n] = fibonacci(n-1) + fibonacci(n-2)
        return fib[n]

T = int(sys.stdin.readline())

for i in range(T):
    fib = {}
    count_z = 0
    count_o = 0
    N = int(sys.stdin.readline())
    fibonacci(N)
    print(count_z, count_o)

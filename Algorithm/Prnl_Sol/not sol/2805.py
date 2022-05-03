import sys

def binary_search(target, data):
    start = 1
    end = max(data)

    while start <= end:
        mid = (start + end) // 2
        log = 0 

        for i in tree:
            if i >= mid:
                log += i - mid

        if log >= target:
            start = mid + 1
        else:
            end = mid - 1
            
    return end

if __name__ == "__main__":
    N, K = map(int,input().split())
    tree = list(map(int, input().split()))

    tree.sort()
    print(binary_search(K, tree))

from bisect import bisect_left, bisect_right


def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    start = 0
    end = n-1
    while start <= end:
        middle = int((start + end)/2)
        if arr[middle] < middle:

            start = middle + 1
        elif arr[middle] > middle:
            end = middle - 1
        elif arr[middle] == middle:
            print(middle)
            return
    print(-1)
    return 0


solution()

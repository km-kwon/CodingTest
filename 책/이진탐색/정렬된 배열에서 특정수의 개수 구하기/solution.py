from bisect import bisect_left, bisect_right


def solution():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    count = bisect_right(arr, x)-bisect_left(arr, x)
    if count == 0:
        print(-1)
    else:
        print(count)
    return 0


solution()

import heapq


def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    while True:
        n = heapq.heappop(arr)
        if len(arr) >= n:
            for i in range(n-1):
                heapq.heappop(arr)
            count += 1
        else:
            break
    print(count)
    return 0


solution()

from collections import deque

def solution():
    n = int(input())
    arr = list(map(int,input().split()))
    arr[2] += arr[0]
    for i in range(3,n):
        arr[i] += max(arr[i-2], arr[i-3])
    print(max(arr[n-1], arr[n-2]))
    return 0


solution()

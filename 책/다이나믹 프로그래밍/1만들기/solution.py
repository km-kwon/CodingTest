from collections import deque

def solution():
    n = int(input())
    arr = [0]*(n+1)
    arr[1] = 0
    for i in range(2,n+1):
        if i%5 ==0:
            arr[i] = min(arr[i-1], arr[i//5])
            arr[i] += 1
        elif i%3 == 0:
            arr[i] = min(arr[i-1], arr[i//3])
            arr[i] += 1    
        elif i%2 == 0:
            arr[i] = min(arr[i-1], arr[i//2])
            arr[i] += 1
        else:
            arr[i] = arr[i-1]+1
    print(arr[n])
    return 0


solution()

import heapq

def solution():
    arr = list(map(int,input()))
    count = 0
    for i in arr:
        if i == 0 or i == 1 or count == 0:
            count += i
            continue
        count *= i
    print(count)
    return 0


solution()

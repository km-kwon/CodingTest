from collections import deque

def solution():
    n = int(input())
    # 각 강의별 들어야 되는거 있는곳
    arr= [0]*(n+1)
    # 각 강의별 걸리는 시간
    times = [0]*(n+1)
    # 각 강의를 듣는데 걸리는 시간
    result = [0]*(n+1)
    for i in range(1,n+1):
        data = list(map(int,input().split()))
        data = deque(data)
        time = data.popleft()
        times[i] = time
        data.pop()
        arr[i] = data
    for i in range(1, n+1):
        if len(arr[i]) ==0:
            result[i] = times[i]
        else:
            for j in arr[i]:
                if result[j] != times[j]:
                    result[i] += result[j]
                if result[i] < times[j]:
                    result[i] = times[j]
            result[i] += times[i]
    return 0


solution()

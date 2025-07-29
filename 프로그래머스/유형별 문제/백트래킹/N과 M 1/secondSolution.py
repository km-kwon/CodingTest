from collections import deque
global iseUsed
N, M = map(int,input().split())
isUsed = [False] * N

def back(count, result):
    if count == M:
        print(" ".join(map(str, result)))
        return
    
    for i in range(N):
        if not isUsed[i]:
            isUsed[i] = True
            result.append(i+1)

            back(count+1, result)

            isUsed[i] = False
            result.pop()
back(0,[])
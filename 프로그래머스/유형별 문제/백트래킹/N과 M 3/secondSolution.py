from collections import deque

N,M = map(int,input().split())

def back(n,m,result):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    for i in range(1, n+1):
        result.append(i)
        back(n,m,result)
        result.pop()
    return

back(N,M,[])
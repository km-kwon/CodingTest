### 연구소 3

성공 코드

```
from collections import deque
import copy

N,activeCount = map(int,input().split())
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))

minTime = 1e9

dx = [0,1,0,-1]
dy = [-1,0,1,0]
virus = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus.append([False,(i,j)])

def bfs(virus):
    global arr, dx, dy, N, minTime
    visited = [[False] * N for _ in range(N)]
    queue = deque()
    curTime = 0
    for check,(i,j) in virus:
        if check:
            queue.append((i,j))
            visited[i][j] = True
    for i in range(N):
        for  j in range(N):
            if arr[i][j] == 1:
                visited[i][j] = True
    while queue:
        afterQueue = deque()
        for cy,cx in queue:
            visited[cy][cx] = True
            for i in range(4):
                ny = cy+dy[i]
                nx = cx+dx[i]
                if ny >= 0 and ny < N and nx >=0 and nx < N:
                    if visited[ny][nx] == False:
                        if arr[ny][nx] == 0 or arr[ny][nx] == 2:
                            if not (ny,nx) in afterQueue:
                                afterQueue.append((ny,nx))
        temp = copy.deepcopy(visited)
        for check,(i,j) in virus:
            temp[i][j] = True
        flag = False
        if not afterQueue:
            for i in range(N):
                for j in range(N):
                    if temp[i][j] == False:
                        return
        else:
            for i in range(N):
                if flag:
                    break
                for j in range(N):
                    if temp[i][j] == False:
                        flag = True
                        break
        if flag:
            curTime +=1
            if curTime > minTime:
                return
            queue = afterQueue
        else:
            break
    minTime = min(curTime,minTime)
    return

def active(start, virus, curVirusCount):
    global activeCount
    if curVirusCount < activeCount:
        for i in range(start,len(virus)):
            virus[i][0] = True
            active(i+1, virus, curVirusCount+1)
            virus[i][0] = False
    elif curVirusCount == activeCount:
        bfs(virus)
    return

active(0,virus,0)

if minTime == 1e9:
    print(-1)
else:
    print(minTime)


```

# 사용 개념

-   그래프 이론
-   브루트포스 알고리즘
-   그래프 탐색
-   너비 우선 탐색

---

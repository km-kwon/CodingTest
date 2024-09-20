### 인구이동

성공 코드

```
from collections import deque

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def solution():
    n, l,r = map(int,input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int,input().split())))
    row = len(arr)
    col = len(arr[0])
    day= 0

    while True:
        cur = 1
        tmp = [[-1]*col for _ in range(row)]
        dic = {}
        flag = 0
        for i in range(row):
            for j in range(col):
                if tmp[i][j] != -1:
                    continue
                else:
                    queue = deque()
                    queue.append((i,j))
                    dic[cur] = [0,0]
                    while queue:
                        cy,cx = queue.popleft()
                        tmp[cy][cx] = cur
                        dic[cur][0] +=1
                        dic[cur][1] += arr[cy][cx]
                        for dir in range(4):
                            ny = cy + dy[dir]
                            nx = cx + dx[dir]
                            if ny >= 0 and ny <row and nx >= 0 and nx < col:
                                if  abs(arr[cy][cx] - arr[ny][nx]) >= l and abs(arr[cy][cx] - arr[ny][nx]) <= r and not (ny,nx) in queue and tmp[ny][nx] != cur:
                                    queue.append((ny,nx))
                                    flag = 1
                    cur+=1
        for i in range(row):
            for j in range(col):
                if tmp[i][j] == -1:
                    continue
                else:
                    arr[i][j] = dic[tmp[i][j]][1] // dic[tmp[i][j]][0]
        if flag == 0:
            print(day)
            return
        day +=1




solution()

```

# 사용 개념

-   bfs
-   구현
-   그래프이론
-   그래프 탐색
-   시뮬레이션

---

# 새겨놔야 할점

-   연합이라는 것을 잘 파악했어야함

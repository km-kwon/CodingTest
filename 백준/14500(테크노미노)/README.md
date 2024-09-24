### 테크노미노

성공 코드

```
import copy
from collections import deque
n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

maxValue = 0


dx = [0,1,0,-1]
dy = [-1,0,1,0]

def find(count, visited, cx,cy):
    global maxValue
    global arr
    if count == 4:
        total = 0
        for i in visited:
            total += arr[i[0]][i[1]]
        maxValue = max(maxValue, total)
        return
    for dir in range(4):
        nx = cx + dx[dir]
        ny = cy + dy[dir]
        if nx>=0 and nx<m and ny >=0 and ny < n and not (ny,nx) in visited:
            visited.append((ny,nx))
            find(count+1, visited, nx, ny)
            visited.pop()


def plus(cx,cy):
    global maxValue
    global arr
    temp = []
    for dir in range(4):
        nx = cx + dx[dir]
        ny = cy + dy[dir]
        if nx>=0 and nx<m and ny >=0 and ny < n:
            temp.append(arr[ny][nx])
    if len(temp) >=3:
        temp.sort(reverse=True)
        maxValue = max(maxValue, arr[cy][cx] + temp[0] + temp[1]+temp[2])



for i in range(n):
    for j in range(m):
        visited = deque()
        visited.append((i,j))
        find(1,visited,j,i)
        plus(j,i)
print(maxValue)


```

# 사용 개념

-   구현
-   브루트포스
-   백트래킹

---

# 새겨놔야 할점

-   시간복잡도 레전드 찍음

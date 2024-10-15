### 아기상어

성공 코드

```
from collections import deque


N = int(input())
arr = []
for  i in range(N):
    arr.append(list(map(int,input().split())))

cury, curx = 0,0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            cury = i
            curx = j
            arr[cury][curx] = 0

def findEat(starty, startx, arr, size):
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    canEat = []
    queue = deque()
    queue.append((starty,startx,0))
    visit = [[False]*N for _ in range(N)]
    canEat = []
    while queue:
        cury, curx, distance = queue.popleft()
        if arr[cury][curx] < size and arr[cury][curx] > 0 and not (cury,curx,distance) in canEat:
            canEat.append((cury,curx, distance))
        for i in range(4):

            ny = cury + dy[i]
            nx = curx + dx[i]
            if ny >= 0 and ny < N and nx >= 0 and nx < N:
                if arr[ny][nx] <= size and visit[ny][nx] == False and not (ny,nx) in queue:
                    queue.append((ny,nx, distance + 1))
                    visit[ny][nx] = True
    return canEat

time = 0
size = 2
fishCount = 0
while True:
    # 일단 먹을 수 있는 물고기 찾아
    canEat = findEat(cury,curx,arr, size)
    if canEat:
        canEat = sorted(canEat, key = lambda x : (x[2], x[0], x[1]))
        cury = canEat[0][0]
        curx = canEat[0][1]
        time += canEat[0][2]
        arr[cury][curx] = 0
        fishCount += 1
        if fishCount == size:
            size += 1
            fishCount = 0
    else:
        break

print(time)

```

# 사용 개념

-   시뮬레이션
-   bfs

---

# 새겨놔야 할점

-   bfs 큐에 넣을때 True로 변경

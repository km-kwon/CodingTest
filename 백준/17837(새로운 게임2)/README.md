### 새로운 게임2

성공 코드

```
ffrom collections import deque

dx = [1,-1,0,0]
dy = [0,0,-1,1]
N,K = map(int,input().split())
arr = []

# 현재 말의 위치
loc = [0]*K
# 판의 상태
status = [[deque() for _ in range(N)] for _ in range(N)]

for i in range(N):
    arr.append(list(map(int,input().split())))

for i in range(K):
    r,c,dir = map(int,input().split())
    loc[i] = [r-1,c-1,dir-1]
    status[r-1][c-1].append(i)

turn = 1
while turn<=1000:
    breakFlag = False
    for i in range(K):
        cury = loc[i][0]
        curx = loc[i][1]
        curdir = loc[i][2]

        ny = cury + dy[curdir]
        nx = curx + dx[curdir]
        # 일단 파란색인지 영역밖인지 확인
        if ny < 0 or ny >=N or nx <0 or nx >= N or arr[ny][nx] == 2:
            if curdir == 0:
                curdir = 1
            elif curdir == 1:
                curdir = 0
            elif curdir ==2:
                curdir = 3
            elif curdir == 3:
                curdir = 2
            ny = cury + dy[curdir]
            nx = curx + dx[curdir]
            loc[i][2] = curdir
        if ny>=0 and ny < N and nx >=0 and nx<N and arr[ny][nx] != 2:
            move = deque()
            resultMove = deque()
            flag = 0
            for j in status[cury][curx]:
                if j == i:
                    flag = 1
                    move.append(j)
                    continue
                if flag == 1:
                    move.append(j)
                else:
                    resultMove.append(j)
            status[cury][curx] = resultMove
            if arr[ny][nx] == 0:
                for j in move:
                    status[ny][nx].append(j)
                    loc[j][0] = ny
                    loc[j][1] = nx
            elif arr[ny][nx] == 1:
                for j in range((-len(move) + 1), 1):
                    status[ny][nx].append(move[-j])
                    loc[move[-j]][0] = ny
                    loc[move[-j]][1] = nx
            if len(status[ny][nx])>=4:
                breakFlag = True
    if breakFlag:
        break
    turn += 1

if turn > 1000:
    print(-1)
else:
    print(turn)
```

# 사용 개념

-   구현
-   시뮬레이션

---

# 새겨놔야 할점

-   시간복잡도 계산

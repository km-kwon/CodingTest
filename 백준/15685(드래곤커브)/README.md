### 사다리 조작

성공 코드

```
import copy

minvalue = 4
colNum = 0
rowNum = 0
def findResult(state):
    for i in range(colNum):
        cur = i
        for j in range(rowNum):
            if state[cur][j] != -1:
               cur = state[cur][j]
        if cur != i:
            return False
    return True

def check(count, state,startCol):
    global minvalue
    if findResult(state) and count < minvalue:
        minvalue= min(count, minvalue)
        return
    elif count+1 < minvalue:
        for i in range(startCol, colNum-1):
            for j in range(rowNum):
                if state[i][j] != -1 or state[i+1][j] != -1:
                    continue
                else:
                    state[i][j] = i+1
                    state[i+1][j] = i
                    check(count+1,state,i)
                    state[i][j] = -1
                    state[i+1][j] = -1

    return

def solution():
    n, m, h = map(int,input().split())
    # 각 i번에 세로 (index) 몇번째 점 이음(배열)
    state = [[-1]*h for _ in range(n)]
    global colNum, rowNum
    colNum = len(state)
    rowNum = len(state[0])
    for i in range(m):
        where, start = map(int,input().split())
        state[start-1][where-1] = start
        state[start][where-1] = start-1

    check(0, state,0)

    if minvalue<=3:
        print(minvalue)
    else:
        print(-1)
    return

solution()
```

# 사용 개념

-   구현
-   브루트포스 알고리즘
-   백트래킹
-   온몸 비틀기

---

# 새겨놔야 할점

-   copy는 시간복잡도를 매우 잡아먹는다
-   재귀를 콜할때 배열은 콜 이후 원상복귀하면 복사할 필요가 없다.
-   온몸비틀기

### [PCCP 기출문제] 2번 석유 시추

---

성공 코드

```
from collections import deque
def solution(land):

    col = len(land[0])
    row = len(land)
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    resultDic = []
    for i in range(row):
        for j in range(col):
            if land[i][j] == 1:
                queue = deque()
                land[i][j] = 0
                queue.append((i,j))
                amount = 1
                smallx, bigx = j,j
                while queue:
                    cy,cx = queue.popleft()
                    for dir in range(4):
                        ny = cy + dy[dir]
                        nx = cx + dx[dir]
                        if ny >= 0 and ny < row and nx >= 0 and nx < col:
                            if land[ny][nx] == 1:
                                queue.append((ny,nx))
                                land[ny][nx] = 0
                                amount += 1
                                if nx > bigx:
                                    bigx = nx
                                if nx < smallx:
                                    smallx = nx
                resultDic.append((smallx,bigx, amount))
    dic = {}
    for small, big, amount in resultDic:
        for i in range(small, big+1):
            if not i in dic:
                dic[i] = amount
            else:
                dic[i] += amount

    return max(dic.values())


```

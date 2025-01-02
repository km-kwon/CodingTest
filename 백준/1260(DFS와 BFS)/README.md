### DFS와 BFS

성공 코드

```
from collections import deque

N,M,V = map(int,input().split())

arr = [[-1 for _ in range(N)]for _ in range(N)]
DFS_VISIT = [False] * N
BFS_VISIT = [False] * N
for i in range(M):
    node, line = map(int,input().split())
    arr[node-1][line-1] = 1
    arr[line-1][node-1] = 1

# DFS
queue = deque()
queue.append(V)
DFS_RESULT = []
while queue:
    cur = queue.pop() - 1
    DFS_VISIT[cur] = True
    if not cur+1 in DFS_RESULT:
        DFS_RESULT.append(cur+1)
    temp = []
    for i in range(N):
        if arr[cur][i] == 1 and DFS_VISIT[i] == False:  
            # 여기서 추가되는건 아직 방문 안했고 길이 있는거
            temp.append(i)
    # 스택에 넣기 위해서 내림차순
    temp = sorted(temp,reverse=True)
    for i in temp:
        queue.append(i+1)


# BFS
queue = deque()
queue.append(V)
BFS_RESULT = []
while queue:
    cur = queue.popleft() - 1
    BFS_VISIT[cur] = True
    if not cur+1 in BFS_RESULT:
        BFS_RESULT.append(cur+1)
    temp = []
    for i in range(N):
        if arr[cur][i] == 1 and BFS_VISIT[i] == False and not i in temp:
            temp.append(i)
    temp.sort()
    for i in temp:
        queue.append(i+1)

for i in range(len(DFS_RESULT)):
    print(DFS_RESULT[i], end=' ')
print()
for i in range(len(BFS_RESULT)):
    print(BFS_RESULT[i], end=" ")


```

# 사용 개념

-   DFS, BFS

---

# 새겨놔야 할점

-   오랜만에 푸니까 재밌네

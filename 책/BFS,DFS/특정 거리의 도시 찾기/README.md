### 특정 거리의 도시 찾기

성공 코드

```
from collections import deque

def solution():
    n,m,k,x = map(int, input().split())
    distance = [1e9]*(n+1)
    distance[0] = 0
    distance[x] = 0
    edge = [[] for _ in range(n+1)]
    queue = deque()
    queue.append(x)
    result = []
    for i in range(m):
        src, dst = map(int, input().split())
        edge[src].append(dst)
    while queue:
        cur = queue.popleft()
        for i in edge[cur]:
            if distance[i] > distance[cur] + 1:
                distance[i] = distance[cur] + 1
                queue.append(i)
    for i in range(len(distance)):
        if distance[i] == k:
            result.append(i)
    if len(result) == 0:
        print(-1)
        return
    for i in result:
        print(i)
    return 0


solution()


```

# 사용 개념

-   무난한 bfs 문제
-   1e9의 활용성은 참 높다

---

### 배달

---

성공 코드

```
from collections import deque

def solution(N, road, K):
    answer = 0
    dic = [[] for _ in range(N+1)]
    for i in road:
        dic[i[0]].append([i[1], i[2]])
        dic[i[1]].append([i[0], i[2]])
    check = [-1] * (N+1)
    check[1] = 0
    que = deque()
    que.append(1)
    while que:
        cur = que.popleft()
        for node, dist in dic[cur]:
            if check[node] == -1 or (check[node] > check[cur] + dist):
                check[node] = check[cur] + dist
                que.append(node)
    for i in range(1, N+1):
        if check[i] <= K:
            answer += 1
    return answer
```

회고

- 일정 노드에서의 거리를 구하는 다익스트라 알고리즘
- BFS로 사용하려고 했지만 중복되는 경우 발생시 문제
- 그렇기에 그냥 전체 간선에 대해서 조사
- 새롭게 갱신될 경우 해당 노드 재탐색

### 전력망 둘로 나누기

---

성공 코드

```
from collections import deque

def solution(n, wires):
    answer = -1
    wires.sort()
    for i in range(len(wires)):
        wire_info = [[] for _ in range(n+1)]
        que = deque()
        count = [0,0]
        cur = 0
        check = [-1] * (n+1)
        for j in range(len(wires)):
            if j == i:
                continue
            wire_info[wires[j][0]].append(wires[j][1])
            wire_info[wires[j][1]].append(wires[j][0])
        for j in range(1,n+1):
            if check[j] == -1:
                check[j] = 1
                count[cur] +=1
                for k in wire_info[j]:
                    if check[k]==-1:
                        check[k] = 1
                        count[cur] += 1
                        que.append(k)
                while que:
                    cur_node = que.popleft()
                    for k in wire_info[cur_node]:
                        if check[k] == -1:
                            check[k] = 1
                            count[cur] += 1
                            que.append(k)
            cur = 1
        if answer == -1:
            answer = abs(count[0] - count[1])
            continue
        if abs(count[0] - count[1]) < answer and answer != -1:
            answer = abs(count[0] - count[1])
    return answer

```

사용 개념

- BFS 사용
- 100 이라 for 문 많이써도 됬네

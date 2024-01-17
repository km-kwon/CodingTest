### 네트워크

---

성공 코드

```
def solution(n, computers):
    answer = 0
    check = [0] * n
    for node in range(len(check)):
        if check[node] == 1:
            continue
        tmp = []
        tmp.append(node)
        check[node] = 1
        while tmp:
            cur = tmp.pop(0)
            for next in range(len(computers[cur])):
                if check[next] == 0:
                    if computers[cur][next] == 1:
                        tmp.append(next)
                        check[next] = 1
        answer += 1
    return answer
```

사용 개념

- BFS 근점 노드 우선 탐색
- Stack 활용하여 해결
- DFS 해결 방법은 재귀로 해결

---

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
- 그리디에서는 스택을 자주 사용할것 같음
- 앞과 뒤만 비교해서 최적해를 찾는과정 => stack이 좋을듯
- answer[:-1] 은 마지막만 뺴고 리턴
- 배열 문자열로 ''.join
---

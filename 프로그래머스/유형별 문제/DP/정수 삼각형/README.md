### 정수 삼각형

---

성공 코드

```
def solution(triangle):
    answer = [[] for i in triangle]
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            answer[i].append(0)
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            if i == 0 and j == 0:
                answer[i][j] = triangle[i][j]
                continue
            if j == 0:
                answer[i][j] = answer[i-1][j] + triangle[i][j]
                continue
            if j == len(triangle[i])-1:
                answer[i][j] = answer[i-1][j-1] + triangle[i][j]
                continue
            answer[i][j] = max((answer[i-1][j-1]),
                               (answer[i-1][j])) + triangle[i][j]
    return max(answer[-1])

```

사용 개념

- dp 사용
- 그 전 내용 배열 저장 및 해결
---


인상 깊었던 코드

```
def solution(triangle):
    dp = []
    for t in range(1, len(triangle)):
        for i in range(t+1):
            if i == 0:
                triangle[t][0] += triangle[t-1][0]
            elif i == t:
                triangle[t][-1] += triangle[t-1][-1]
            else:
                triangle[t][i] += max(triangle[t-1][i-1], triangle[t-1][i])
    return max(triangle[-1])
```

사용 개념
- 간단하게 triangle 배열 갱신
- 추가로 메모리 할당 필요 없음
- 시간 복잡도 감소

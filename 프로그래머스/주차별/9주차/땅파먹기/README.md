### 땅파먹기

---

성공 코드

```
def solution(land):
    answer = 0
    for i in range(1, len(land)):
        for j in range(len(land[i])):
            cur = land[i][j]
            for k in range(len(land[i-1])):
                if j == k:
                    continue
                if (cur + land[i-1][k]) > land[i][j]:
                    land[i][j] = cur + land[i-1][k]
    return max(land[i])

```

회고

- dp의 가장 대표적인 문제
- 그리디를 고민했지만 dp 로 해결

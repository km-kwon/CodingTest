### 최고의 집합

---

성공 코드

```
def solution(n, s):
    answer = []
    while n >0:
        if s < n:
            answer.append(-1)
            break
        val = int(s/n)
        s = s - val
        n = n-1
        answer.append(val)
    return answer



```

회고

- 수학적인 측면에서 생각하면 쉽게 풀음
- 보통 수학적인 요소를 생각하게 하면 level 3인듯

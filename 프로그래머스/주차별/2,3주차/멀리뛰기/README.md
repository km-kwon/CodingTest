### 멀리 뛰기

---

성공 코드

```
def solution(n):
    answer = [0] * (n+1)

    if n < 3:
        return n
    answer[1] = 1
    answer[2] = 2
    for i in range(3, n+1):
        answer[i] = (answer[i-1] + answer[i-2]) % 1234567
    return answer[n]

```

회고

- 전형적인 dp 문제
- n이 더 길어도 될듯

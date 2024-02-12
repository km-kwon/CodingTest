### 2xn 타일링

---

성공 코드

```
def solution(n):
    answer = 0
    dp = [0]*n
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

    return dp[n-1]

```

회고

- dp의 가장 대표적인 문제
- 점화식을 활용하여 해결

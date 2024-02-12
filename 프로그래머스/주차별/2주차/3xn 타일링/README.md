### 3xn 타일링

---

성공 코드

```
def solution(n):
    if n % 2 != 0:
        return 0
    dp = [0] * int(n/2)
    dp[0] = 3
    dp[1] = 11
    for i in range(3, int(n/2)+1):
        dp[i-1] = (dp[i-2] * 3 + sum(dp[0:i-2]) * 2 + 2) % 1000000007
    return dp[int(n/2)-1]


```

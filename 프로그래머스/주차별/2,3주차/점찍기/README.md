### 점찍기

---

성공 코드

```
import math


def solution(k, d):
    answer = 0
    for i in range(0, d+1, k):
        max_y = int(math.sqrt(d**2 - i**2))
        answer += (int(max_y/k)+1)
    return answer

```

회고

- 전형적인 수학적 접근 법
- 계산만 잘하고 구하는 공식만 생각하면 쉽게 풀림

### 게임 개발

성공 코드

```
from collections import deque


def solution():
    n = list(map(int, input()))
    half = len(n)/2
    left = 0
    right = 0
    for i in range(len(n)):
        if i < half:
            left += n[i]
        else:
            right += n[i]
    if left == right:
        print("LUCKY")
        return 0
    print("READY")
    return 0


solution()


```

사용 개념

- 못풀면 안되는 구현 문제

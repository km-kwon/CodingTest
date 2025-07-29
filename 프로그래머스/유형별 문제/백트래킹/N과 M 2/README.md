### N과 M 1

---

성공 코드

```
from collections import deque

global isUsed
N, M = map(int,input().split())
isUsed = [False] * N
def back(count, result):
    if count == M:
        print(" ".join(map(str, result)))
        return
    for i in range(N):
        if len(result) > 0 and result[-1] > i+1:
            continue
        if not isUsed[i]:
            isUsed[i] = True
            result.append(i+1)

            back(count+1, result)

            isUsed[i] = False
            result.pop()
    return

back(0,[])

```

사용 개념

- 오랜만에 푸니까 재밌네
- 단순 조건 하나 추가긴 해

```

```

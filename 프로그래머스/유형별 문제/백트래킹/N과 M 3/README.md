### N과 M 1

---

성공 코드

```
from collections import deque

N,M = map(int,input().split())

def back(n,m,result):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    for i in range(1, n+1):
        result.append(i)
        back(n,m,result)
        result.pop()
    return

back(N,M,[])
```

사용 개념

```
- 오랜만에 푸니까 재밌네
- 단순 조건 하나 추가긴 해

```

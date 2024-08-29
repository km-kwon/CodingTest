### 곱하기 혹은 더하기

성공 코드

```
import heapq

def solution():
    arr = list(map(int,input()))
    count = 0
    for i in arr:
        if i == 0 or i == 1 or count == 0:
            count += i
            continue
        count *= i
    print(count)
    return 0


solution()


```

사용 개념

-   일종의 그리디
-   각 상황에서 최선의 선택

---

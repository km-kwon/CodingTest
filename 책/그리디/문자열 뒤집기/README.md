### 문자열 뒤집기

성공 코드

```
import heapq

def solution():
    arr = list(map(int,input()))
    cur = arr[0]
    count = 0
    flag = False
    for i in range(1, len(arr)):
        if cur != arr[i] and flag == False:
           flag = True
           count += 1
        elif cur != arr[i] and flag == True:
            flag = False
        cur  = arr[i]
    print(count)
    return 0


solution()

```

사용 개념

-   이것도 그리디긴 함
-   좀더 쉬운 방법이 있을까?

---

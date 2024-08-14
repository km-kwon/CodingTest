### 개미 전사

성공 코드

```
from collections import deque

def solution():
    n = int(input())
    arr = list(map(int,input().split()))
    arr[2] += arr[0]
    for i in range(3,n):
        arr[i] += max(arr[i-2], arr[i-3])
    print(max(arr[n-1], arr[n-2]))
    return 0


solution()

```

# 사용 개념

-   단순한 DP문제
-   일단 큰수부터 먼저 나눠보는게 핵심

---

# 새겨놔야 할점

-   그전에 쓰였던 값을 다시 쓸수 있느냐?
-   어떤 연산 다음에 이전값을 사용한다면 DP인거임

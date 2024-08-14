### 1만들기

성공 코드

```
from collections import deque

def solution():
    n = int(input())
    arr = [0]*(n+1)
    arr[1] = 0
    for i in range(2,n+1):
        if i%5 ==0:
            arr[i] = min(arr[i-1], arr[i//5])
            arr[i] += 1
        elif i%3 == 0:
            arr[i] = min(arr[i-1], arr[i//3])
            arr[i] += 1
        elif i%2 == 0:
            arr[i] = min(arr[i-1], arr[i//2])
            arr[i] += 1
        else:
            arr[i] = arr[i-1]+1
    print(arr[n])
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

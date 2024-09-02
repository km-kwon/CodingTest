### 정수 삼각형

성공 코드

```
from collections import deque

def solution():
    n = int(input())
    arr = []
    for i in range(n):
        temp = list(map(int,input().split()))
        arr.append(temp)
    for i in range(1,n):
        for j in range(len(arr[i])):
            if j == 0:
                arr[i][j] = arr[i][j]+ arr[i-1][j]
            elif j == (len(arr[i])-1):
                arr[i][j] = arr[i][j] +arr[i-1][j-1]
            else:
                arr[i][j] = arr[i][j] + max(arr[i-1][j], arr[i-1][j-1])
    print(max(arr[n-1]))
    return 0


solution()


```

# 사용 개념

-   단순한 DP문제
-   위에서 아래로~~

---

# 새겨놔야 할점

-   그전에 쓰였던 값을 다시 쓸수 있느냐?
-   어떤 연산 다음에 이전값을 사용한다면 DP인거임

### 효율적인 화폐구성

성공 코드

```
from collections import deque


def solution():
    n, price = map(int,input().split(' '))
    arr= [-1]*(price+1)
    numbers = []
    numbers.sort()
    for i in range(n):
        numbers.append(int(input()))
    for i in numbers:
        for j in range(1,price+1):
            if j % i==0 and arr[j] == -1:
                arr[j] = j//i
            elif j % i ==0 and arr[j] > j//i:
                arr[j] = j//i
            elif arr[j] == -1 and j-i > 0 and arr[j-i] != -1:
                arr[j] = arr[j-i] + 1
            elif j-i >0 and arr[j-i] != -1 and arr[j] > arr[j-i] +1:
                arr[j] = arr[j-i] + 1
    print(arr[price])
solution()


```

# 사용 개념

-   조금 어려웠던 dp 문제
-   생각해줘야했던 경우의 수가 있기에 헷갈림
-   최적화는 고민해야할듯

---

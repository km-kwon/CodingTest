### 고정점 찾기

성공 코드

```
from bisect import bisect_left, bisect_right


def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    start = 0
    end = n-1
    while start <= end:
        middle = int((start + end)/2)
        if arr[middle] < middle:
            start = middle + 1
        elif arr[middle] > middle:
            end = middle - 1
        elif arr[middle] == middle:
            print(middle)
            return
    print(-1)
    return 0


solution()

```

사용 개념

- 뭐 딱히 어려운건 없는 이진 탐색
- 정렬되어 있으면 이진 탐색 고려

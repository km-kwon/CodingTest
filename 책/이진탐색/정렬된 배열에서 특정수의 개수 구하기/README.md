### 정렬된 배열에서 특정수의 개수 구하기

성공 코드

```
from bisect import bisect_left, bisect_right


def solution():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    count = bisect_right(arr, x)-bisect_left(arr, x)
    if count == 0:
        print(-1)
    else:
        print(count)
    return 0


solution()

```

사용 개념

- bisect 라이브러리 발견
- 완전 간편하게 삽입 index 반환

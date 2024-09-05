### 시험 감독

성공 코드

```
from collections import deque

def solution():
    #시험장의 개수
    n = int(input())
    # 각 시험장 응시자 수
    arr = list(map(int,input().split()))
    # 총감독관 가능 b 부감독관 가능 c
    b,c = map(int,input().split())
    count  = 0
    for i in arr :
        cur = i
        cur -= b
        count += 1
        if cur <=0 :
            continue
        if cur % c == 0:
            count += cur // c
            continue
        count += ((cur//c) + 1)
    print(count)
    return

solution()


```

# 사용 개념

-   그리디

---

# 새겨놔야 할점

-   브론즈2 문제인데 10분 걸림

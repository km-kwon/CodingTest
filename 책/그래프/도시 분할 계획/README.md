### 도시분할 계획

성공 코드

```

def solution():
    n, m = map(int, input().split())
    arr = [1] * (n+1)
    arr[0] = 0
    costInfo = []

    curCost = 0
    for i in range(m):
        a, b, cost = map(int, input().split())
        heapq.heappush(costInfo, (cost, a, b))
    cost = 0
    while sum(arr) != 0:
        curCost, curA, curB = heapq.heappop(costInfo)
        if arr[curA] == 0 and arr[curB] == 0:
            continue
        arr[curA] = 0
        arr[curB] = 0
        cost += curCost
    print(cost-curCost)
    return 0


solution()
```

사용 개념

-   heap정렬 활용해서 해결

---

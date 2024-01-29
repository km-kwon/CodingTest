### 야근 지수

---

성공 코드

```
import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    heap = []
    for i in works:
        heap.append(-i)
    heapq.heapify(heap)

    for i in range(n):
        heapq.heappush(heap, -(-(heapq.heappop(heap)) - 1))

    sum1 = 0
    for i in heap:
        sum1 += i*i
    return sum1
```

사용 개념

- 최대 힙 큐 사용
- 이론적 접근은 맞았지만 효율성 검사를 위한 최대 힙 사용

---

인상 깊었던 코드

```
def noOvertime(n, works):
  if n>=sum(works):
    return 0;

  while n > 0:
    works[works.index(max(works))] -= 1
    n -= 1

  result = sum([w ** 2 for w in works])

  return result
```

사용 개념

- sum을 활용한 방법
- sum 내의 for 문 사용

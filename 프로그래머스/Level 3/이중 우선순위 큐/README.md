### 이중 우선순위 큐

---

성공 코드

```
import heapq


def solution(operations):
    arr = []
    for i in operations:
        operation = i[0]
        num_value = int(i[2:])
        if operation == "I":
            heapq.heappush(arr, num_value)
            continue
        if operation == "D" and num_value == 1:
            if len(arr) != 0:
                max_value = max(arr)
                arr.remove(max_value)
                continue
        if operation == "D" and num_value == -1:
            if len(arr) != 0:
                heapq.heappop(arr)
    if len(arr) == 0:
        answer = [0, 0]
    else:
        answer = [max(arr), heapq.heappop(arr)]
    return answer

```

사용 개념

- heapq 사용
- 하지만 두개의 큐를 사용하고 싶었음
- 동기화 문제에 대해 고민

---

### 택배 상자

---

성공 코드

```
from collections import deque
def solution(order):
    answer = 0
    i = 1
    stack = deque()
    cur = 0
    while i != (len(order)+1):
        stack.append(i)
        while stack and stack[-1] == order[cur]:
            answer +=1
            cur +=1
            stack.pop()
        i +=1
    return answer
```

사용 개념

- 스택 사용하였지만 문제 이해하는데 어려움을 겪음

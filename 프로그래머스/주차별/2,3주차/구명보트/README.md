### 구명 보트

---

성공 코드

```
def solution(people, limit):
    answer = 0
    people.sort()
    left, right = 0, len(people)-1
    while left <= right:
        if people[right] + people[left] <= limit and len(people) != 1:
            left += 1
            right -= 1
            answer += 1
            continue
        right -= 1
        answer += 1
    return answer

```

회고

- pop(0)은 시간 복잡도 N이 걸림
- 시간 초과 해결하기 위해 배열수정 X
- 다만 값을 참조하기 위한 포인터만 선언하여 시간 복잡도 줄임

인상깊은 코드

```
from collections import deque

def solution(people, limit):
    result = 0
    deque_people = deque(sorted(people))

    while deque_people:
        left = deque_people.popleft()
        if not deque_people:
            return result + 1
        right = deque_people.pop()
        if left + right > limit:
            deque_people.appendleft(left)
        result += 1
    return result
```

- 이중포인터 개념이 들어가긴 했음
- queue로 구현
- 이중포인터를 큐로 구현한것 => 가독성 높아질듯

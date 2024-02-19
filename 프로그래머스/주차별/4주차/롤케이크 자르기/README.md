### 롤케이크 자르기

---

성공 코드

```
import collections


def solution(topping):
    answer = 0
    topping = collections.deque(topping)
    dic1 = collections.Counter(topping)
    dic2 = {}
    while len(dic1) >= len(dic2):
        cur = topping.popleft()
        dic1[cur] -= 1
        if dic1[cur] == 0:
            del dic1[cur]
        if not cur in dic2:
            dic2[cur] = 1
        else:
            dic2[cur] += 1
        if len(dic1) == len(dic2):
            answer += 1

    return answer

```

회고

- 해쉬 및 배열 순회
- 시간복잡도 고려하여 최선의 답 도출

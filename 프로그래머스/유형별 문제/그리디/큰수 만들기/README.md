### 큰 수 만들기

---

성공 코드

```
import heapq


def solution(scoville, K):
    heapq.heapify(scoville)

    answer = 0
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        heapq.heappush(scoville, heapq.heappop(
            scoville) + heapq.heappop(scoville)*2)
        answer += 1
    return answer

```

사용 개념

- 힙 정렬
- heapq 외부 라이브러리 사용

---

사용 개념

- 기존 파이썬 sort 사용시 시간 초과
- heapq 정렬을 사용하면 nlogn의 시간복잡도로 더 빠르게 해결 가능

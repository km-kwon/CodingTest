### 징검다리 건너기

---

성공 코드

```
def solution(stones, k):
    answer = 0
    left, right = 0, max(stones)
    while left <= right:
        mid = (left+right)//2
        count = 0
        for i in range(0, len(stones)):
            if stones[i] - mid <= 0:
                count += 1
                if count == k:
                    break
                continue
            count = 0
        if count < k:
            left = mid+1
            continue
        answer = mid
        right = mid-1
    return answer
```

사용 개념

- 이분 탐색
- 추가로 슬라이딩 윈도우 풀이도 존재

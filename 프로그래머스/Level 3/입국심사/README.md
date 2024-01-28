### 입국 심사

---

성공 코드

```
def solution(n, times):
    answer = 0
    left = min(times)
    right = max(times) * n
    while left <= right:
        mid = (left+right)//2
        passed = 0
        for time in times:
            passed += mid // time
            if passed >= n:
                break
        if passed >= n:
            answer = mid
            right = mid - 1
            continue
        if passed < n:
            left = mid + 1
    return answer
```

사용 개념

- BFS 사용
- 발상의 전환

---

실패 코드

```
def solution(n, times):
    answer = 0
    left = min(times)
    right = max(times) * n
    while left <= right:
        mid = (left+right)//2
        passed = 0
        for time in times:
            passed += mid // time
            if passed >= n:
                break
        if passed >= n:
            answer = mid
            right = mid - 1
            continue
        if passed < n:
            left = mid + 1
    return answer
```

사용 개념

- 이분 탐색
- 이분 탐색의 조건 (배열의 길이)

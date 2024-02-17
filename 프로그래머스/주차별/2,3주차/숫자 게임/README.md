### 숫자 게임

---

성공 코드

```
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    j = 0
    for i in range(len(A)):
        if A[j] < B[i]:
            answer += 1
            j += 1
    return answer

```

회고

- 이분탐색으로 해결하려고 했지만 실패
- 원인이 뭘까 고민하지만 실패

---

실패 코드

```
def solution(A, B):
    answer = 0
    B.sort()
    for i in A:
        left, right = 0, len(B)-1
        while left <= right:
            mid = (left + right) // 2
            if B[mid] <= i:
                left = mid + 1
                continue
            if B[mid] > i:
                right = mid - 1
        if B[mid] > i:
            answer += 1
        B.pop(mid)
    return answer
```

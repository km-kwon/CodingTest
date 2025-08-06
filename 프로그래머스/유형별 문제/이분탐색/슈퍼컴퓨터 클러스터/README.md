### 슈퍼컴퓨터 클러스터

---

성공 코드

```
n, b = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()

left, right = arr[0], 10000000000

result = 0
while left<=right:
    count = 0
    mid = (left+right) // 2
    for i in arr:
        if i < mid:
            count += (mid-i) ** 2
        if count > b:
            break
        if i >= mid:
            break
    if count > b:
        right = mid-1
    else:
        result = mid
        left = mid + 1
print(result)

```

사용 개념

- 이분탐색
- 크게 어렵진 않음

```

```

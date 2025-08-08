### 커넥티드 카 실험

---

성공 코드

```
from collections import deque


n, s = map(int,input().split())
init = list(map(int,input().split()))
oil = list(map(int,input().split()))

# 초기 위치 및 잔여 연료
left=0
can_left = 1e9
right=0
can_right = 0
result = []

queue = deque()

# 각 위치에 있는 자동차의 번호
arr = [[] * n for _ in range(n)]
for i in range(n):
    # 자동차 정보 = (위치, 오일, 차번호(id))
    arr[i] = (init[i]-1,oil[i],i+1)
    if i+1 == s:
        left,right= i-1,i+1
        queue.append(i)
        result.append(arr[i][2])


while queue:
    cur = queue.popleft()
    can_left = min(arr[cur][0] - arr[cur][1], can_left)
    can_right = max(arr[cur][0] + arr[cur][1], can_right)
    while right < n and can_right >= arr[right][0]:
        result.append(arr[right][2])
        queue.append(right)
        right += 1
    while  left >= 0 and can_left <= arr[left][0]:
        result.append(arr[left][2])
        queue.append(left)
        left-=1

result.sort()
print(*result)

```

```
사용 개념

- 이중 포인터

```

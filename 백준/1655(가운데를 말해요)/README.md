### 가운데를 말해요

성공 코드

```
import heapq

n = int(input())
left = []
right = []
value = []
for i in range(1,n+1):
    temp = int(input())

    heapq.heappush(left, -temp)
    #일단 left에 넣고 둘이 같거나 왼쪽이 하나 더 많게
    if abs(len(left) - len(right)) == 2:
        heapq.heappush(right, (-heapq.heappop(left)))
    # 홀수면 왼쪽에서 하나 가져가서 보여주면 됨
    if i % 2 == 1 :
        if left and right:
            if (-left[0] > right[0]):
                heapq.heappush(right, -heapq.heappop(left))
                heapq.heappush(left, -heapq.heappop(right))
        value.append(-left[0])
    # 짝수면 양쪽에서 작은거 하나 출력
    elif i % 2 ==0 :
        value.append(min(-left[0], right[0]))

for i in value:
    print(i)

```

# 사용 개념

-   우선순위 큐

---

# 새겨놔야 할점

-   우선순위 큐를 두개 사용하면 중간값을 알 수 있음

### 별자리 만들기기

---

성공 코드

```
import math
import heapq

result = 0

n = int(input())

arr = []
star_parent = [0] * n
for i in range(n):
    star_parent[i] = i

heap = []

def find_parent(star_num):
    if star_parent[star_num] != star_num:
        return find_parent(star_parent[star_num])
    return star_num

for i in range(n):
    x,y = map(float, input().split())
    arr.append((x,y))

for star_1 in range(n):
    for star_2 in range(star_1,n):
        if star_1 == star_2:
            continue
        distance = math.sqrt(((arr[star_1][0]-arr[star_2][0])**2) + ((arr[star_1][1]-arr[star_2][1])**2))
        heapq.heappush(heap,(distance, star_1, star_2 ))

while heap:
    min_distance, star_1, star_2 = heapq.heappop(heap)
    star_1_parent = find_parent(star_1)
    star_2_parent = find_parent(star_2)

    # 작은놈으로 부모 설정
    if star_1_parent == star_2_parent:
        continue
    elif star_1_parent > star_2_parent:
        star_parent[star_1_parent] = star_2_parent
    elif star_1_parent < star_2_parent:
        star_parent[star_2_parent] = star_1_parent
    result += min_distance

print(round(result, 2))
```

사용 개념

- 부모노드를 바꿀때 최상위 부모를 바꿔야함

오답 코드

```elif star_1_parent > star_2_parent:
        star_parent[star_1] = star_2_parent
    elif star_1_parent < star_2_parent:
        star_parent[star_2] = star_1_parent
```

정답 코드

```elif star_1_parent > star_2_parent:
        star_parent[star_1_parent] = star_2_parent
    elif star_1_parent < star_2_parent:
        star_parent[star_2_parent] = star_1_parent
```

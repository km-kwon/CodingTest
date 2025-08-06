### 여왕개미

---

성공 코드

```
import bisect

q = int(input())

arr = []
for i in range(q):
    arr.append(list(map(int,input().split())))

house = []
house_info = {

}
cur_house_number = 0
for query in arr:
    if query[0] == 100:
        temp = query[2:]
        for i in range(len(temp)):
            cur_house_number +=1
            house_info[cur_house_number] = temp[i]
            house.append(temp[i])
        house.sort()
    elif query[0] == 200:
        bisect.insort(house,query[1])
        cur_house_number += 1
        house_info[cur_house_number] = query[1]
    elif query[0] == 300:
        where = house_info[query[1]]
        house.remove(where)
    elif query[0] == 400:
        # 사용할 수 있는 최대 개미
        max_count = query[1]
        # 바로 앞 개미집까지의 거리
        left, right = 0, 1000000000
        cur = 0
        time = 0
        while left<=right:
            mid = (left+right) // 2
            count = 0
            cur = 0
            for i in house:
                if cur < i:
                    count += 1
                    cur = i + mid
                if count > max_count:
                    break
            if count > max_count:
                left = mid+1
            else:
                time = mid
                right = mid-1
        print(time)
```

```
사용 개념

- 이분탐색

```

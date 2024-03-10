### 방문길이

---

성공 코드

```
def solution(dirs):
    cur = [0, 0]
    road = []
    for i in dirs:
        if i == "U":
            next_x, next_y = cur[0], (cur[1] + 1)
            if next_y > 5:
                next_y = 5
                continue
        elif i == "D":
            next_x, next_y = cur[0], (cur[1] - 1)
            if next_y < -5:
                next_y = -5
                continue
        elif i == "L":
            next_x, next_y = (cur[0] - 1), cur[1]
            if next_x < -5:
                next_x = -5
                continue
        elif i == "R":
            next_x, next_y = (cur[0] + 1), cur[1]
            if next_x > 5:
                next_x = 5
                continue
        cur.append(next_x)
        cur.append(next_y)
        cur1 = [cur[2], cur[3], cur[0], cur[1]]
        if not cur in road and not cur1 in road:
            road.append([cur[0], cur[1], cur[2], cur[3]])
        cur.pop(0)
        cur.pop(0)
    return len(road)
```

회고

- 단순 구현 문제로 예상

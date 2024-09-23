### 톱니바퀴

성공 코드

```
from collections import deque
import copy

# 2랑 6
gear = []
for i in range(4):
    gear.append(deque(list(map(int, input()))))


def turn(gearNum, dir):
    # 기어1
    global gear
    # 시계
    if dir == 1:
        last = gear[gearNum].pop()
        gear[gearNum].appendleft(last)
    # 반시계
    elif dir == -1:
        first = gear[gearNum].popleft()
        gear[gearNum].append(first)
    return


n = int(input())
for i in range(n):
    gearNum, dir = map(int, input().split())
    gearNum -= 1
    temp = []
    isRound = [False]*4

    for j in range(4):
        temp.append(gear[j].copy())

    if gearNum == 0:
        turn(0, dir)
        isRound[0] = True
        dir *= -1
        if temp[0][2] != temp[1][6]:
            turn(1, dir)
            isRound[1] = True
            dir *= -1
        if temp[1][2] != temp[2][6] and isRound[1]:
            turn(2, dir)
            isRound[2] = True
            dir *= -1
        if temp[2][2] != temp[3][6] and isRound[2]:
            turn(3, dir)
            isRound[3] = True

    elif gearNum == 1:
        turn(1, dir)
        isRound[1] = True
        dir *= -1
        if temp[1][2] != temp[2][6]:
            turn(2, dir)
            isRound[2] = True
        if temp[0][2] != temp[1][6]:
            turn(0, dir)
        if temp[2][2] != temp[3][6] and isRound[2]:
            dir *= -1
            turn(3, dir)
            isRound[3] = True

    elif gearNum == 2:
        turn(2, dir)
        isRound[2] = True
        dir *= -1
        if temp[1][2] != temp[2][6]:
            turn(1, dir)
            isRound[1] = True
        if temp[2][2] != temp[3][6]:
            turn(3, dir)
            isRound[3] = True
        if temp[0][2] != temp[1][6] and isRound[1]:
            dir *= -1
            turn(0, dir)

    elif gearNum == 3:
        turn(3, dir)
        isRound[3] = True
        dir *= -1
        if temp[2][2] != temp[3][6]:
            turn(2, dir)
            isRound[2] = True
            dir *= -1
        if temp[1][2] != temp[2][6] and isRound[2]:
            turn(1, dir)
            isRound[1] = True
            dir *= -1
        if temp[0][2] != temp[1][6] and isRound[1]:
            turn(0, dir)
            isRound[1] = True
            dir *= -1
count = 0
score = 1
for i in gear:
    if i[0] == 1:
        count += score
    score *= 2
print(count)

```

# 사용 개념

-   빡구현

---

# 새겨놔야 할점

-   뭔가 최적화 가능할것 같긴한데 연속적인 느낌이라 힘듦

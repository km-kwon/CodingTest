### 공원 산책

---

성공 코드

```
def solution(park, routes):
    answer = []
    len_w = len(park[0])-1
    len_h = len(park)-1
    loc_x = 0
    loc_y = 0
    for i in range(len(park)):
        check = park[i].find("S")
        if check != -1:
            loc_x = i
            loc_y = check
    for i in routes:
        flag = False
        order = i.split()
        if order[0] == "E":
            if (loc_y + int(order[1])) > len_w:
                flag = True
                continue

            for check in range(int(order[1])):
                if park[loc_x][loc_y + check + 1] == "X":
                    flag = True
                    break

            if flag == False:
                loc_y = loc_y + int(order[1])

        if order[0] == "W":

            if (loc_y - int(order[1])) < 0:
                flag = True
                continue

            for check in range(int(order[1])):
                if park[loc_x][loc_y - (check + 1)] == "X":
                    flag = True
                    break

            if flag == False:
                loc_y = loc_y - int(order[1])

        if order[0] == "S":

            if (loc_x + int(order[1])) > len_h:
                flag = True
                continue

            for check in range(int(order[1])):
                if park[loc_x + check + 1][loc_y] == "X":
                    flag = True
                    break

            if flag == False:
                loc_x = loc_x + int(order[1])

        if order[0] == "N":

            if (loc_x - int(order[1])) < 0:
                flag = True
                continue

            for check in range(int(order[1])):
                if park[loc_x - (check + 1)][loc_y] == "X":
                    flag = True
                    break

            if flag == False:
                loc_x = loc_x - int(order[1])
    answer.append(loc_x)
    answer.append(loc_y)
    return answer

```

사용 개념

- 2 차원 배열
- 배열 find
- append

---

다른 사람 코드 중 인상 깊었던 것

```
 def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = {"N": (-1, 0), "W": (0, -1), "E": (0, 1), "S": (1, 0)}

    def move(self, park, direction, distance):
        i, j = self.g[direction]
        x, y = self.x + (i * distance), self.y + (j * distance)
        if x < 0 or y < 0 or x >= len(park) or y >= len(park[0]):
            return park
        elif "X" in park[x][min(self.y, y) : max(self.y, y) + 1] or "X" in [
            row[y] for row in park[min(self.x, x) : max(self.x, x)]
        ]:
            return park
        park[self.x][self.y] = "O"
        park[x][y] = "S"
        self.x = x
        self.y = y
        return park

    @classmethod
    def detect_start_dogs_location(self, park):
        for i, row in enumerate(park):
            for j, item in enumerate(row):
                if item == "S":
                    return i, j


def solution(park, routes):
    park = [list(row) for row in park]
    x, y = Dog.detect_start_dogs_location(park)

    dog = Dog(x, y)

    for route in routes:
        direction, distance = route.split()
        park = dog.move(park, direction, int(distance))

    return [dog.x, dog.y]
```

사용 개념

- 이사람은 각 방향에 대한 정의를 미리 정의해놓음
- 움직일때마다 반복. min max를 적절하게 활용함
- 움직일때마다 각 위치에 대한 정의를 새로함.

# 새겨놔야 할점

- 최적화된 풀이를 고민해봐야할 듯
- 너무나 브루트포스 방법만을 고민함
- 수학적 센스를 생각해보는 고민을 해봐야할듯

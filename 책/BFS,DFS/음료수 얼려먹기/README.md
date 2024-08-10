### 음료수 얼려먹기

성공 코드

```
from collections import deque


def solution():
    queue = deque()
    queue.append((0, 0))
    # dir은 멋대로 제시해 주는것이 아니다.
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    height, width = map(int, input().split(' '))
    visited = [[0]*width for _ in range(height)]

    arr = []
    for i in range(height):
        arr.append(list(map(int, input())))

    count = 0
    for i in range(height):
        for j in range(width):
            if visited[i][j] == 1 or arr[i][j] == 1:
                continue
            queue.append((i, j))
            while queue:
                cur_y, cur_x = queue.popleft()
                visited[cur_y][cur_x] = 1
                for dir in range(4):
                    next_y = cur_y+dy[dir]
                    next_x = cur_x+dx[dir]
                    if next_y < height and next_y >= 0 and next_x < width and next_x >= 0:
                        if visited[next_y][next_x] == 0 and arr[next_y][next_x] == 0 and ((next_y, next_x) not in queue):
                            queue.append((next_y, next_x))
            count += 1
    print(count)
    return 0

```

사용 개념

- map을 이용해서 할당
- bfs개념
- 최적화 고민해야 할듯

---

# 새겨놔야 할점

- bfs 오랜만에 풀어서 헷갈림
- 너무 오래걸렸음

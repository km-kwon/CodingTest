### 마법의 숲 탐색

---

성공 코드

```
from collections import deque
import copy

r, c, k = map(int, input().split())
# 실질적 시작은 3부터
forest = [[1001] + [0]*c + [1001] for i in range(r+3)]
forest.append([1001]*(c+2))
golem_dir = [(-1,0), (0,1), (1,0), (0,-1)]

dic_out = {}
result = 0
def canDown(center_row, center_col):
    flag = False
    if forest[center_row + 2][center_col] == 0 and forest[center_row + 1][center_col-1] == 0 and forest[center_row+1][center_col+1] == 0:
        flag = True
    return flag

def canLeft(center_row, center_col):
    flag = False
    # 왼쪽 가능한지
    if forest[center_row][center_col-2] == 0 and forest[center_row-1][center_col-1] == 0 and forest[center_row+1][center_col-1] == 0:
        # 왼쪽 아래 가능한지
        if forest[center_row+2][center_col-1] == 0 and forest[center_row+1][center_col-2] == 0:
            flag = True
    return flag

def canRight(center_row, center_col):
    flag = False
    # 오른쪽 가능한지
    if forest[center_row][center_col+2] == 0 and forest[center_row-1][center_col+1] == 0 and forest[center_row+1][center_col+1] == 0:
        # 오른쪽 아래 가능한지
        if forest[center_row+2][center_col+1] == 0 and forest[center_row+1][center_col+2] == 0:
            flag = True
    return flag

def clear_forest():
    global forest,dic_out
    forest = [[1001] + [0]*c + [1001] for _ in range(r+3)]
    forest.append([1001]*(c+2))
    dic_out = {}
    return

def move(start_row, start_col, dir, id):
    global result, r, c
    if canDown(start_row, start_col):
        move(start_row+1, start_col, dir, id)
        return
    elif canLeft(start_row, start_col):
        dir -= 1
        if dir == -1:
            dir = 3
        move(start_row+1, start_col-1, dir, id)
        return
    elif canRight(start_row, start_col):
        dir += 1
        if dir == 4:
            dir = 0
        move(start_row+1, start_col+1, dir, id)
        return
    else:
        # 이동끝
        forest[start_row][start_col] = id
        for i in range(4):
            ny = start_row + golem_dir[i][0]
            nx = start_col + golem_dir[i][1]
            if dir == i:
                dic_out[(ny,nx)] = True
            forest[ny][nx] = id
        # row 판단
        for i in range(3):
            for j in range(1, c+1):
                if forest[i][j] != 0:
                    clear_forest()
                    return
        max_row = -1
        queue = deque()
        queue.append((start_row, start_col, forest[start_row][start_col]))
        visited = {}
        visited[(start_row, start_col)] = forest[start_row][start_col]
        while queue:
            cur_y, cur_x, cur_id = queue.pop()
            for i in range(4):
                ny = cur_y + golem_dir[i][0]
                nx = cur_x + golem_dir[i][1]
                if forest[ny][nx] == cur_id and not (ny,nx) in visited:
                    queue.append((ny,nx,forest[ny][nx]))
                    visited[(ny,nx)] = forest[ny][nx]
                    max_row = max(max_row, ny-2)
                elif (cur_y,cur_x) in dic_out and  dic_out[(cur_y,cur_x)] and forest[ny][nx] != 1001 and forest[ny][nx] != 0 and not (ny,nx) in visited:
                    queue.append((ny,nx,forest[ny][nx]))
                    visited[(ny,nx)] = forest[ny][nx]
                    max_row = max(max_row,ny-2)
        result += max_row
        return

for id in range(1, k+1):
    start, d = map(int, input().split())
    # start col 좌표 = start + 1
    move(1, start, d, id)

print(result)
```

사용 개념

- 시뮬레이션
- 삼성 기출문제

---

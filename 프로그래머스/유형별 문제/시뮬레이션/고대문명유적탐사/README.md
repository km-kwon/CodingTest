### 고대 문명 유적 탐사

성공 코드

```
from collections import deque
import copy


k,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(5)]

#채워넣을수있는 유물의 수
remain = deque(list(map(int,input().split())))
degrees= [90,180,270]
dir = [(-1,0), (0,1), (1,0), (0,-1)]

def find_count_treasure(matrix):
    total_count = 0
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 0:
                continue
            else:
                get_list = [(i,j)]
                queue = deque([(i,j, matrix[i][j])])
                matrix[i][j] = 0
                while queue:
                    cr,cc,cur_value = queue.popleft()
                    for (dr,dc) in dir:
                        nr,nc = cr+dr, cc+dc
                        if 0<=nr<5 and 0<=nc<5 and cur_value == matrix[nr][nc]:
                            get_list.append((nr,nc))
                            matrix[nr][nc] = 0
                            queue.append((nr,nc,cur_value))
                if len(get_list) >= 3:
                    total_count += len(get_list)
    return total_count


def find_treasure(matrix):
    total_count = 0
    visited = {}
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 0:
                continue
            else:
                visited[(i,j)] = True
                get_list = [(i,j)]
                queue = deque([(i,j, matrix[i][j])])
                while queue:
                    cr,cc,cur_value = queue.popleft()
                    for (dr,dc) in dir:
                        nr,nc = cr+dr, cc+dc
                        if 0<=nr<5 and 0<=nc<5 and cur_value == matrix[nr][nc] and not (nr,nc) in visited:
                            get_list.append((nr,nc))
                            visited[(nr,nc)] = True
                            queue.append((nr,nc,cur_value))
                if len(get_list) >= 3:
                    for (cr,cc) in get_list:
                        matrix[cr][cc] = 0
                    total_count += len(get_list)
    return total_count, matrix

def fill_maxtrix(matrix):
    for j in range(5):
        for i in range(4,-1,-1):
            if matrix[i][j] == 0 and remain:
                matrix[i][j] = remain.popleft()
    return matrix


def rotate(matrix, row_start, row_end, col_start, col_end, degree, flag):
    sub_matrix = [row[col_start:col_end+1] for row in matrix[row_start: row_end+1]]
    size = row_end - row_start + 1
    for i in range(size):
        for j in range(size):
            if degree == 90:
                ni, nj = j, size-1-i
            elif degree ==180:
                ni, nj = size-1-i, size-1-j
            elif degree == 270:
                ni,nj = size-1-j, i
            matrix[row_start + ni][col_start+nj] = sub_matrix[i][j]
    if flag:
        return find_count_treasure(matrix)
    else:
        get_treasure = 0
        after_get_matrix = matrix
        while True:
            temp, after_get_matrix = find_treasure(after_get_matrix)
            if temp > 0:
                get_treasure += temp
                after_get_matrix = fill_maxtrix(after_get_matrix)
            else:
                break
        return after_get_matrix, get_treasure
for turn in range(k):
    result = 0
    treasure = 0
    selected_degree = 1e9
    find_row, find_col = -1,-1
    # row 1~3 col 1~3의 모든 회전 다해봐야함
    for degree in degrees:
        for center_col in range(1,4):
            for center_row in range(1,4):
                # 1차 획득 후 상태, 얻은 유물 수
                count_get_treasure = rotate(copy.deepcopy(arr), center_row-1, center_row+1, center_col-1, center_col+1, degree, True)
                if count_get_treasure > treasure:
                    treasure = count_get_treasure
                    find_row, find_col,selected_degree = center_row, center_col,degree
    if treasure == 0:
        break
    else:
        arr, count = rotate(copy.deepcopy(arr), find_row-1, find_row+1, find_col-1, find_col+1, selected_degree, False)
        result += count
    print(result, end=' ')

```

# 사용 개념

- 시뮬레이션

---

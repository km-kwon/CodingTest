### 2048(EASY)

성공 코드

```
from collections import deque
import copy


def top(arr, n):
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        cur = -1
        cur_loc = 0
        for j in range(n):
            if arr[j][i] == 0:
                continue
            else:
                if cur == -1:
                    cur = arr[j][i]
                elif cur == arr[j][i]:
                    cur = -1
                    result[cur_loc][i] = arr[j][i]*2
                    cur_loc += 1
                elif cur != arr[j][i]:
                    result[cur_loc][i] = cur
                    cur_loc += 1
                    cur = arr[j][i]
                # 만약 맨 끝이야 그럼 그거 append
        if j == (n-1) and cur != -1:
            result[cur_loc][i] = (cur)
    return result


def bottom(arr, n):
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        cur = -1
        cur_loc = n-1
        for j in range(-(n-1), 1):
            if arr[-j][i] == 0:
                continue
            else:
                if cur == -1:
                    cur = arr[-j][i]
                elif cur == arr[-j][i]:
                    cur = -1
                    result[cur_loc][i] = arr[-j][i]*2
                    cur_loc -= 1
                elif cur != arr[-j][i]:
                    result[cur_loc][i] = cur
                    cur_loc -= 1
                    cur = arr[-j][i]
        # 만약 맨 끝이야 그럼 그거 append
        if cur != -1:
            result[cur_loc][i] = (cur)
    return result


def left(arr, n):
    result = []
    # 세로 확인
    for i in range(n):
        temp = [0]*n
        cur = -1
        cur_loc = 0
        # 가로 확인하면서 일단 합친 배열 생성
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                continue
            else:
                if cur == -1:
                    cur = arr[i][j]
                # cur과 지금 값이 같아(합쳐야 할 상황)
                elif cur == arr[i][j]:
                    cur = -1
                    temp[cur_loc] = (arr[i][j]*2)
                    cur_loc += 1
                elif cur != arr[i][j]:
                    temp[cur_loc] = (cur)
                    cur_loc += 1
                    cur = arr[i][j]
        if cur != -1:
            temp[cur_loc] = cur
        result.append(temp)
    return result


def right(arr, n):
    result = []
    for i in range(n):
        temp = [0]*n
        cur = -1
        cur_loc = n-1
        for j in range(1, len(arr[i])+1):
            if arr[i][-j] == 0:
                continue
            else:
                if cur == -1:
                    cur = arr[i][-j]
                elif cur == arr[i][-j]:
                    cur = -1
                    temp[cur_loc] = arr[i][-j]*2
                    cur_loc -= 1
                elif cur != arr[i][-j]:
                    temp[cur_loc] = (cur)
                    cur_loc -= 1
                    cur = arr[i][-j]
        if j == (len(arr[i])) and cur != -1:
            temp[cur_loc] = (cur)
        result.append(temp)
    return result


def checkMax(count, n, arr):
    maxValue = 0
    if count < 5:
        rightValue = right(arr, n)
        leftValue = left(arr, n)
        topValue = top(arr, n)
        bottomValue = bottom(arr, n)
        return max([checkMax(count+1, n, rightValue), checkMax(count+1, n, topValue), checkMax(count+1, n, leftValue), checkMax(count+1, n, bottomValue)])
    else:
        maxValue = max(map(max, arr))
        return maxValue


def solution():
    n = int(input())
    table = []
    for i in range(n):
        table.append(list(map(int, input().split())))
    # print(bottom(table,n))
    print(checkMax(0, n, table))
    return


solution()

```

# 사용 개념

- 구현
- 브루트포스 알고리즘
- 시뮬레이션
- 백트래킹

---

# 새겨놔야 할점

- 각각 구현을 시행
- 조건문 확인 잘하기

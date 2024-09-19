### 이차원배열과 연산

성공 코드

```
import copy


def cal(row, col, arr):
    temp = copy.deepcopy(arr)
    maxLen = 0
    result = []
    for i in range(row):
        row_result = []
        dic = {}
        sort_temp = []
        for j in range(col):
            if temp[i][j] == 0:
                continue
            if not temp[i][j] in dic:
                dic[temp[i][j]] = [1, temp[i][j]]
            else:
                dic[temp[i][j]][0] += 1
        for j in dic.values():
            sort_temp.append(j)
        sort_temp = sorted(sort_temp, key=lambda x: (x[0], x[1]))
        for j in sort_temp:
            row_result.append(j[1])
            row_result.append(j[0])
        maxLen = max(maxLen, len(row_result))
        result.append(row_result)
    for i in range(len(result)):
        for j in range(maxLen-len(result[i])):
            result[i].append(0)
    for i in range(len(result)):
        result[i] = result[i][:100]
    return result


def solution():
    r, c, k = map(int, input().split())
    r = r-1
    c = c-1
    time = 0
    arr = []
    for i in range(3):
        arr.append(list(map(int, input().split())))
    while True:
        row = len(arr)
        col = len(arr[0])
        if row > r and col > c:
            if arr[r][c] == k and time <= 100:
                print(time)
                break
            elif time > 100:
                print(-1)
                break
        if row >= col:
            arr = cal(row, col, arr)
            time += 1
        elif row < col:
            arr = list(zip(*arr))
            arr = cal(col, row, arr)
            arr = list(zip(*arr))
            time += 1

    return


solution()


```

# 사용 개념

- 배열 전치
- 시간초과 너무 오래걸림...

---

# 새겨놔야 할점

- 해답을 처음으로 봤던 문제
- 자신감 파이팅

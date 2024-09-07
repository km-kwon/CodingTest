### 경사로

성공 코드

```

def checkLine(arr, l):
    minLength = len(arr)
    on = [0] * len(arr)
    for i in range(len(arr)-1):
        if abs(arr[i+1] - arr[i]) > 1:
            return False
        # 다음칸이 높아짐
        if arr[i+1] > arr[i] and (arr[i+1] - arr[i]) == 1:
            start = i
            end = i
            while start-1 >= 0 and arr[start-1] == arr[end]:
                start -= 1
            minLength = min(minLength, end-start+1)
            for j in range(end-l+1, end+1):
                if j >= 0:
                    on[j] += 1
        # 다음칸이 낮아짐
        elif arr[i+1] < arr[i] and (arr[i]-arr[i+1]) == 1:
            start = i+1
            end = i+1
            while end < len(arr)-1 and arr[end+1] == arr[start]:
                end += 1
            minLength = min(minLength, end-start + 1)
            for j in range(start, start+l):
                if j < len(arr)-1:
                    on[j] += 1
    for i in on:
        if i > 1:
            return False
    if minLength < l:
        return False
    return True


def solution():
    n, l = map(int, input().split())
    arr = []
    for i in range(n):
        temp_arr = list(map(int, input().split()))
        arr.append(temp_arr)

    count = 0
    for i in range(n):
        if checkLine(arr[i], l):
            count += 1
    for i in range(n):
        if checkLine([arr[j][i] for j in range(n)], l):
            count += 1
    print(count)
    return


solution()


```

# 사용 개념

- 구현

---

# 새겨놔야 할점

- 각각의 조건을 명확히 세워야 할듯 함.

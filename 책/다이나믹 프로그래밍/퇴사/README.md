### 퇴사

성공 코드

```

def solution():
    n = int(input())
    arr = []
    for i in range(n):
        cost, money = map(int,input().split())
        arr.append([cost,money,0])
    for i in range(n):
        #현재 시간 + 걸리는 시간이 날짜보다 길면 안됨
        if i + arr[i][0] < n:
            if arr[i+arr[i][0]][2] < arr[i][1] + arr[i][2]:
                arr[i+arr[i][0]][2] = arr[i][1] + arr[i][2]
    max = 0
    for i in range(n):
        if max < arr[i][2]:
            max = arr[i][2]
    print(max)
    return 0


solution()

```

# 사용 개념

-   큰 어려움은 없었음
-   특이한 점은 앞을 관찰하는게 아니라 뒤의 값을 수정

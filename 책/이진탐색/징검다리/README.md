### 공유기 찾기

성공 코드

```

def solution():
    n,c = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    arr.sort()
    start, end= 1, arr[-1]+arr[0]
    max_value= 0
    while start<=end:
        mid = (end+start)//2
        count = 1
        cur = arr[0]
        for i in arr:
            if (i-cur)>=mid:
                count+=1
                cur = i
        if count >= c:
            max_value = max(max_value, mid)
            start = mid+1
        else:
            end = mid-1
    print(max_value)
    return 0


solution()


```

사용 개념

-   각 집 사이의 거리를 이진탐색으로 탐색

### 떡볶이 떡 만들기

성공 코드

```
ddef solution():
    n, length = map(int, input().split())
    arr = list(map(int,input().split(' ')))
    end = max(arr)
    start = 1
    avg = int((end+start)/2)
    while True:
        sum = 0
        avg = int((end+start)/2)
        for i in arr:
            if i>avg:
                sum += (i-avg)
        if sum > length:
            start = avg+1
        elif sum<length:
            end = avg-1
        elif sum == length:
            break
        if end < start:
            break
    print(avg)


    return 0
```

사용 개념

-   이진 탐색 개념을 실시
-   이진 탐색을 실시할 경우 log n 만큼의 시간이 걸림

---

# 새겨놔야 할점

-   이진탐색은 그 유형을 외워놓는게 좋을듯
-   약간 길이가 뭔가 있고 그 사이에서 찾는거면 하는거인듯

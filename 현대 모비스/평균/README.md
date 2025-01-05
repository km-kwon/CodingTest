### 평균

성공 코드

```
N = int(input())
arr = list(map(int, input().split()))
maxValue = max(arr)
for i in range(N):
    arr[i] = arr[i] / maxValue * 100

print(sum(arr) / N)


```

# 사용 개념

-   그냥 입력받고 출력력

---

# 새겨놔야 할점

-   그래도 감잡기 쉬운 문제

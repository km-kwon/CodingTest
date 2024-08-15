### 바닥공사

성공 코드

```

def solution():
    n = int(input())
    arr = [0]*(n+1)
    arr[1] = 1
    if n >= 2:
        arr[2] = 3
        if n >= 3:
            for i in range(3, n+1):
                arr[i] = arr[i-1] + arr[i-2]*2
    print(arr[n] % 796796)


solution()

```

# 사용 개념

- 단순한 DP문제
- 점화식 세우는게 중요함

---

### 회전초밥

성공 코드

```
N, d, k, c = map(int, input().split())

arr = [0] * (N + k)
dic = {}
maxVal = 0
for i in range(N):
    arr[i] = int(input())

for i in range(N, N + k):
    arr[i] = arr[i - N]
    if arr[i - N] not in dic:
        dic[arr[i - N]] = 1
    else:
        dic[arr[i - N]] += 1

if c not in dic:
    maxVal = max(0, len(dic) + 1)
else:
    maxVal = max(0, len(dic))

for i in range(N):
    dic[arr[i]] -= 1
    if dic[arr[i]] == 0:
        del dic[arr[i]]
    if arr[i + k] not in dic:
        dic[arr[i + k]] = 1
    else:
        dic[arr[i + k]] += 1

    if c not in dic:
        maxVal = max(maxVal, len(dic) + 1)
    else:
        maxVal = max(maxVal, len(dic))

print(maxVal)

```

# 사용 개념

-   슬라이딩 윈도우우

---

# 새겨놔야 할점

-   시간복잡도 고려해서 풀었긴 함
- 처음에는 이중탐색으로 풀려고 했는데 너무 오래걸려서 다른 해결책 확인

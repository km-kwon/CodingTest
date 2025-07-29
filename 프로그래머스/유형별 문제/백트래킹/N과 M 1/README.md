### N과 M 1

---

성공 코드

``from collections import deque
global iseUsed
N, M = map(int,input().split())
isUsed = [False] \* N

def back(count, result):
if count == M:
print(" ".join(map(str, result)))
return

    for i in range(N):
        if not isUsed[i]:
            isUsed[i] = True
            result.append(i+1)

            back(count+1, result)

            isUsed[i] = False
            result.pop()

back(0,[])

```

사용 개념

- 오랜만에 푸니까 재밌네
- 백트래킹 문제
- 현재값 표기하고 한번 돌리고 빼고
```

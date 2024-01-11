### 같은 숫자는 싫어

---

성공 코드

```
def solution(arr):
    answer = []
    cur = 0
    answer.append(arr[0])
    for i in range(0, len(arr)):
        if answer[cur] != arr[i]:
            answer.append(arr[i])
            cur += 1
    print(answer)
    return answer
```

사용 개념

- stack 개념 사용 

---

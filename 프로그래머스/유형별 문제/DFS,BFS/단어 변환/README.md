### 단어 변환

---

성공 코드

```
def solution(numbers, target):
    answer = 0
    result = [0]
    for i in numbers:
        tmp = []
        for j in result:
            tmp.append(j + i)
            tmp.append(j - i)
        result = tmp
    for i in result:
        if i == target:
            answer += 1
    print(answer)
    return answer
```

사용 개념

- 스택
- 시간 복잡도
- 배열 덮어 씌움으로서 모든 경우의 수 탐구

---

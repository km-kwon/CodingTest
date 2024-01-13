### 기능 개발

---

성공 코드

```
def solution(progresses, speeds):
    answer = []
    day = 0
    while progresses:
        count = 0
        day += 1
        for i in range(len(progresses)):
            if speeds[i] * day + progresses[i] < 100:
                break
            count += 1
        for i in range(count):
            progresses.pop(0)
            speeds.pop(0)
        if count != 0:
            answer.append(count)

    return answer
```

사용 개념

- pop 사용


---

다른 사람 코드 중 인상 깊었던 것

```
def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
```

사용 개념

- for 문의 단계를 한번 더 줄임
- 기존 생각에서 조금만 더 고민하면 나올 수 있던 생각일듯

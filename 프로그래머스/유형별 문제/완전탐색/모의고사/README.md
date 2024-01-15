### 모의고사

---

성공 코드

```
def solution(answers):
    answer = []
    per1 = [1, 2, 3, 4, 5]
    per2 = [2, 1, 2, 3, 2, 4, 2, 5]
    per3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == per1[i % 5]:
            count[0] += 1
        if answers[i] == per2[i % 8]:
            count[1] += 1
        if answers[i] == per3[i % 10]:
            count[2] += 1
    winner = max(count)
    for i in range(len(count)):
        if count[i] == winner:
            answer.append(i+1)
    return answer
```

사용 개념

- 완전 탐색이기 떄문에 별다른 특이사항은 없음
- 나머지 정리 활용하여 해결
- 다른 이들도 나와 비슷한 방법으로 해결

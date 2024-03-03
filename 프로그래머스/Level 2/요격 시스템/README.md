### 요격 시스템


---

성공 코드

```
def solution(targets):
    answer = 1
    targets.sort(key=lambda x: x[1])
    cur = targets[0][1]
    for i in targets:
        if cur > i[0] and cur <= i[1]:
            continue
        else:
            answer += 1
            cur = i[1]
    return answer

```

회고

- 그리디를 이용한 대표적인 문제
- 조건에 부합하지만 약간의 변형 사용

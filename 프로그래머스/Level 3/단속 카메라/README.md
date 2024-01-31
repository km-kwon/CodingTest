### 단속 카메라

---

성공 코드

```
def solution(routes):
    answer = 1
    routes = sorted(routes, key=lambda x: x[1])
    cur_position = routes[0][1]
    for i in routes:
        if cur_position >= i[0] and cur_position <= i[1]:
            continue
        cur_position = i[1]
        answer += 1
    return answer

```

사용 개념

- 겹치는 구간을 세려고 했지만 문제 의도를 파악
- 각 차는 무조건 감시카메라를 설치해야함
- 즉 가장 늦게 설치할때 최대로 많은 차가 겹칠 것임
- greedy 접근법 사용

---

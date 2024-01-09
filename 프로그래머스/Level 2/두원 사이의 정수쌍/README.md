### 두 원사이의 정수 쌍

---

성공 코드

```
import math


def solution(r1, r2):
    answer = 0

    for x in range(1, r2+1):
        y = int(math.sqrt(r2*r2 - x*x))
        if x < r1:
            y1 = math.ceil(math.sqrt(r1*r1 - x*x))
        else:
            y1 = 0
        answer = answer + y - y1+1
    return answer*4
```

사용 개념

- math 외부 라이브러리 사용
- ceil (올림) int(내림) 사용
- 수학적 개념 사용 (피타고라스 y 구하기)


주의 해야했던 점
- 일단 수학적인 계산을 생각하느라 오래걸림
- 의외로 간단하게 풀린다는 점

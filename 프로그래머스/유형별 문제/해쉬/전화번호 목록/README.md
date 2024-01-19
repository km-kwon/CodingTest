### 폰켓몬

---

성공 코드

```
import collections
def solution(nums):
    return min(len(list(collections.Counter(nums))), len(nums)/2)

```

사용 개념

- dictionary 자료형
- collection 라이브러리 사용
- dic의 list 화

---

인상 깊었던 점
- dic을 list 화 시키면 key들로만 이루어진 list가 생성
  
```
Counter({3: 2, 1: 1, 2: 1})
[3, 1, 2]
Counter({3: 3, 2: 2, 4: 1})
[3, 2, 4]
Counter({3: 3, 2: 3})
[3, 2]
```

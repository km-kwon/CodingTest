### 귤 고르기

---

성공 코드

```
import collections

def solution(k, tangerine):
    answer = 0
    dic = collections.Counter(tangerine)
    dic = dict(sorted(dic.items(), key = lambda x:x[1], reverse = True))
    for i in dic.values():
        k -= i
        answer +=1
        if k <= 0:
            break
    return answer
```

회고

- 콜렉션 카운터 문제
- 딕셔너리 정렬 문제

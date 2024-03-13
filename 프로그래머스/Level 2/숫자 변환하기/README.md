### 숫자 변환하기

---

성공 코드

```
def solution(x, y, n):
    answer = 0
    s = set()
    s.add(x)
    while s:
        if y in s:
            return answer
        nxt = set()
        for i in s:
            if i + n <= y:
                nxt.add(i+n)
            if i * 2 <= y:
                nxt.add(i * 2)
            if i * 3 <= y:
                nxt.add(i* 3)
        s = nxt
        answer += 1
    return -1
```

회고

- 집합을 이용한 풀이
- dp로 걱정 안해도 될듯

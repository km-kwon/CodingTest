### 의상

---

성공 코드

```
def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        if dic.get(i[1], -1) == -1:
            dic[i[1]] = 2
            continue
        dic[i[1]] += 1
    for value in dic.values():
        answer *= value

    return answer-1
```

사용 개념

- dictionary 자료형
- collection 라이브러리 사용
- dic values 값 순회


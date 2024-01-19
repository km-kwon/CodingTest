### 폰켓몬

---

성공 코드

```
def solution(phone_book):
    answer = True
    list = dict.fromkeys(phone_book, 0)
    for i in phone_book:
        number = ""
        for j in i:
            number += j
            if number in list and number != i:
                answer = False
    return answer


```

사용 개념

- dictionary 자료형
- collection 라이브러리 사용
- dic의 list화 (fromkeys 사용)

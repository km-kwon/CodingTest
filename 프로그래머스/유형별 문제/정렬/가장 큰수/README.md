### 가장 큰수

---

성공 코드

```
def solution(numbers):
    answer = ''
    list = []
    for i in numbers:
        list.append(str(i))
    list.sort(key=lambda x: x*3, reverse=True)
    return str(int("".join(list)))
```

사용 개념

- 정수의 문자화
- ASCII로 변환하여 비교해야함.
- 문자열로 바꾸고 아스키 값으로 비교

---

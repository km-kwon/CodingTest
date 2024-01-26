### 섬 연결하기

---

성공 코드

```
def solution(number, k):
    answer = []
    for i in number:
        if not answer:
            answer.append(i)
            continue
        while answer and answer[-1] < i and k > 0:
            answer.pop()
            k -= 1
        answer.append(i)
    if k > 0:
        answer = answer[:-k]
    return ''.join(answer)


```

사용 개념

- 스택
- 그리디에서는 스택을 자주 사용할것 같음
- 앞과 뒤만 비교해서 최적해를 찾는과정 => stack이 좋을듯
- answer[:-1] 은 마지막만 뺴고 리턴
- 배열 문자열로 ''.join

---

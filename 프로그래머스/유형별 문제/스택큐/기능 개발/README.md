### 같은 숫자는 싫어

---

성공 코드

```
def solution(participant, completion):
    answer = ''
    value_dic = {}
    for name in participant:
        if (value_dic.get(name, -1)) != -1:
            value_dic[name] += 1
            continue
        value_dic[name] = 1
    for name in completion:
        value_dic[name] -= 1
        if value_dic[name] == 0:
            value_dic.pop(name)
    return list(value_dic)[0]
```

사용 개념

- 해쉬
- 딕셔너리 자료형 사용
- dic pop 사용

---

다른 사람 코드 중 인상 깊었던 것

```
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]

or

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
```

사용 개념

- collection 라이브러리 counter 사용
- counter은 dic에 특화된 함수 \
- 그 외 list나 dic 등 다양한 자료형에 사용할 수 있는 함수들 존재

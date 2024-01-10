### 완주 하지 못한 선수

---

성공 코드

```
def solution(names, yearning, photos):
    value_dic = {}
    answer = []
    for i, name in enumerate(names):
        value_dic[name] = yearning[i]
    for photo in photos:
        each_photo_value = 0
        for person in photo:
            each_photo_value += value_dic.get(person, 0)
            ##값없으면 0 리턴
        answer.append(each_photo_value)
    return answer
```

사용 개념

- dictionary 자료형
- dictionary 자료형 선언 enmerate
- for
- 배열 선언
- 배열 추가
- dic에서 값 없으면 처리 (get)

---

다른 사람 코드 중 인상 깊었던 것

```
def solution(name, yearning, photo):
    dictionary = dict(zip(name,yearning))
    scores = []
    for pt in photo:
        score = 0
        for p in pt:
            if p in dictionary:
                score += dictionary[p]
        scores.append(score)
    return scores
```

사용 개념

- 이사람은 zip을 사용했음

그 외 다른 사람들은 그냥 index로만 사용해서 푼 사람들도 있는데
시간 복잡도 생각하여 dictionary로 풀음

index => O(n^2)
dic => O(n)

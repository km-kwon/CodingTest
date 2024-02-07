### 보석 쇼핑

---

성공 코드

```
def solution(gems):
    answer = [0, len(gems)-1]
    type = len(set(gems))
    dic = {gems[0]: 1}
    left, right = 0, 0
    while left < len(gems) and right < len(gems) and left <= right:
        if len(dic) == type:
            if (answer[1] - answer[0]) > (right-left):
                answer[0], answer[1] = left, right
            dic[gems[left]] -= 1
            if dic[gems[left]] == 0:
                del dic[gems[left]]
            left += 1
            continue
        if len(dic) < type:
            right += 1
            if right >= len(gems):
                break
            if not gems[right] in dic:
                dic[gems[right]] = 1
            else:
                dic[gems[right]] += 1
    answer[0], answer[1] = answer[0] + 1, answer[1]+1
    return answer
```

회고

- 이중포인터를 활용한 풀이
- 0,0에서 시작
- 초기 생각 0, len(gems) 에서 3가지 경우 max취하려고했음

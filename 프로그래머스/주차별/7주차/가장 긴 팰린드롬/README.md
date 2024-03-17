### 가장 긴 팰린드롬

---

성공 코드

```
def solution(s):
    answer = 0
    for i in range(len(s)+1):
        for j in range(i, (len(s)+1)):
            sub = s[i:j]
            pali = sub[::-1]
            if sub == pali and answer <len(pali):
                answer  = len(pali)
    return answer

```

사용 개념

- ::-1을 이용한 배열 거꾸로 배치

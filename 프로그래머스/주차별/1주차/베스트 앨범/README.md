### 베스트 앨범

---

성공 코드

```

def solution(genres, plays):
    answer = []
    info = []
    dic = {}
    dic_count = {}
    for i in range(len(genres)):
        info.append([plays[i], genres[i],  -i])
        if genres[i] in dic:
            dic[genres[i]] += plays[i]
            dic_count[genres[i]] += 1
            continue
        dic[genres[i]] = plays[i]
        dic_count[genres[i]] = 1
    info.sort(reverse=True)
    while dic:
        high_genres = max(dic, key=dic.get)
        count = 0
        for i in info:
            if i[1] == high_genres:
                count += 1
                answer.append(-i[2])
                if count >= 2:
                    break
        dic.pop(high_genres)
        dic_count.pop(high_genres)
    return answer
```

회고

- 문제를 제대로 읽지 않아서 시간이 오래 걸렸다.
- lambda를 사용해서 한번 풀어보자
- 조건을 x:x[0], x[1] 이런식으로
- 첫번째 조건이 같으면 두번째 조건으로 ~~

---

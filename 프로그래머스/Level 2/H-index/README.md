### H-index

---

성공 코드

```
def solution(citations):
    answer = 0
    citations.sort(reverse=True)

    for i in range(len(citations)):
        if (citations[i] < i+1):
            return i

    return len(citations)

```

회고

- 어렵지 않은 정렬 문제

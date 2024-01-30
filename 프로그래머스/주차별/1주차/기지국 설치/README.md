### 기지국 설치

---

성공 코드

```
def solution(n, stations, w):
    answer = 0
    check = []
    can_check = 2*w + 1
    for i in stations:
        start = max(0, i - 1 - w)
        end = min(n - 1, i - 1 + w)
        check.append([start, end])
    cur = -1
    for i in check:
        length = i[0] - cur - 1
        if length % can_check == 0:
            answer += length/can_check
            cur = i[1]
            continue
        answer += length//can_check + 1
        cur = i[1]
    if cur != n-1:
        length = n-1 - cur
        if length % can_check == 0:
            answer += length/can_check
            cur = i[1]
        else:
            answer += length//can_check + 1
            cur = i[1]
    return int(answer)

```

사용 개념

- 시간 복잡도의 이유로 stations의 길이를 활용
- stations의 길이는 10,000이기 때문에 전체 순환

---

실패 코드

```
def solution(n, stations, w):
    answer = 0
    check = [0]*n
    for i in stations:
        for j in range(-w, w+1):
            if i-1+j < 0:
                continue
            try:
                check[i-1+j] = 1
            except IndexError:
                continue
    cur = 0
    while cur < n:
        if check[cur] == 0:
            answer += 1
            cur += ((2*w)+1)
            continue
        cur += 1
    return answer
```

사용 개념

- N이 2억이기 때문에 전체 순회는 불가능
- 다른 수학적 접근 활용
- 그리디를 활용하는 방법 사용
- 거리 계산을 통해 값 계산

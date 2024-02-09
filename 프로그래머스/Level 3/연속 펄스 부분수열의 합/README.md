### 연속 펄스 부분수열의 합

---

성공 코드

```
def solution(sequence):
    sequence2 = sequence[:]
    purse = 1
    for i in range(len(sequence)):
        sequence[i] *= purse
        purse *= -1
        sequence2[i] *= purse
    max_sum = 0
    tmp = 0
    for s in sequence:
        tmp += s
        if tmp < 0:
            tmp = 0
        max_sum = max(max_sum, tmp)
    tmp = 0
    for s in sequence2:
        tmp += s
        if tmp < 0:
            tmp = 0
        max_sum = max(max_sum, tmp)
    return max_sum

=
```

회고

- 문제의 조건을 충분히 읽어보지 않았음
- 그로인해 전혀 다른 알고리즘 작성
- 부분수열의 합을 다루는 사항
- 부분수열의 합 = DP로 접근
- 부분수열의 합? => 이전값 참소??? DP
- 수열의 범위? => 이중 포인터??
- 고민을 좀더 할 필요성을 느낌

실패 코드

```
def solution(sequence):
    answer = 0
    left, right = 0, 1
    max = 0
    start = 0
    if sequence[0] > 0:
        start = 1
    else:
        start = -1
    while right <= len(sequence)-1:
        if sequence[right]*start < 0:
            start = start * -1
            max += abs(sequence[right])
            if right == len(sequence)-1:
                if max > answer:
                    answer = max
            right += 1
            continue
        if left != right-1:
            if max > answer:
                answer = max
        left = right
        max = abs(sequence[left])
        right += 1
    return answer

```

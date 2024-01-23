### 연속된 부분수열의 합

---

성공 코드

```
def solution(sequence, k):
    position = []
    position_value = []
    start = 0
    end = 0
    sum = sequence[0]
    while start <= end and end < len(sequence):
        if sum < k:
            if end+1 == len(sequence):
                break
            end += 1
            sum += sequence[end]
            continue
        if sum > k:
            sum -= sequence[start]
            start += 1
            continue
        if sum == k:
            position_value.append(end-start)
            position.append([start, end])
            if end+1 == len(sequence):
                break
            end += 1
            sum += sequence[end]
    # print(position[position_value.index(min(position_value))])
    return position[position_value.index(min(position_value))]
```

사용 개념

- 이중 포인터 알고리즘
- 시간복잡도 N으로 줄임

---

실패 코드

```
def solution(sequence, k):
    position = []
    position_idx = []
    for i in range(len(sequence)):
        value = 0
        if sequence[i] > k:
            break
        for j in range(i, len(sequence)):
            value += sequence[j]
            if value > k:
                break
            if value == k:
                position.append([i, j])
                position_idx.append(j-i)
                break
    print(position[position_idx.index(min(position_idx))])
    return position[position_idx.index(min(position_idx))]
```

사용 개념

- 시간복잡도 초과로 인한 실패
- 이중 for 문은 사용하지 않는 것이 좋은듯
- 수열의 길이가 긴경우 이중 for 문 사용 X
- 이중 포인터 알고리즘 적극 권장

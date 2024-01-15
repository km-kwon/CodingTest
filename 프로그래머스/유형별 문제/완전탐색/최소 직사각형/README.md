### 최소 직사각형

---

성공 코드

```
def solution(sizes):
    answer = 0
    heights = []
    widths = []
    for i, j in sizes:
        heights.append(max(i, j))
        widths.append(min(i, j))
    return max(heights) * max(widths)


```

사용 개념

- 완전 탐색이기 떄문에 별다른 특이사항은 없음
- 시간복잡도를 줄이기 위해서 배열 추가X 해도 됨

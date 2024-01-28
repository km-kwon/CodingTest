### 부대 복귀

---

성공 코드

```
def solution(n, roads, sources, destination):
    answer = []
    roads.sort()
    cur_road = [[] for i in range(n)]
    for i in (roads):
        cur_road[i[0]-1].append(i[1]-1)
        cur_road[i[1]-1].append(i[0]-1)
    stack = [destination-1]
    check = [-1] * n
    check[destination-1] = 0
    while stack:
        cur_position = stack.pop(0)
        for j in cur_road[cur_position]:
            if check[j] == -1:
                check[j] = check[cur_position]+1
                stack.append(j)
    for i in sources:
        answer.append(check[i-1])
    return answer
```

사용 개념

- BFS 사용
- 발상의 전환

---

실패 코드

```
def solution(n, roads, sources, destination):
    answer = []
    roads.sort()
    cur_road = [[] for i in range(n)]
    for i in (roads):
        cur_road[i[0]-1].append(i[1]-1)
        cur_road[i[1]-1].append(i[0]-1)
    for i in sources:
        stack = [i-1]
        check = [-1] * n
        check[i-1] = 0
        while stack:
            cur_position = stack.pop(0)
            for j in cur_road[cur_position]:
                if check[j] == -1:
                    check[j] = check[cur_position]+1
                    stack.append(j)
        answer.append(check[destination-1])
    return answer
```

사용 개념

- 출발지 기준으로 for 문 수행
- 그로인한 시간복잡도 증가
- 역으로 destination을 기준으로 거리 계산


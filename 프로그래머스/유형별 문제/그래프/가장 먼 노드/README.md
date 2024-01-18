### 가장 먼 노드

---

성공 코드

```
def solution(n, edge):
    answer = 0
    distance = [-1] * n
    distance[0] = 0
    tmp = [0]
    graph = [[] for _ in range(n)]

    for i in edge:
        graph[i[0]-1].append(i[1]-1)
        graph[i[1]-1].append(i[0]-1)
    while tmp:
        cur = tmp.pop(0)
        for i in graph[cur]:
            if distance[i] == -1:
                tmp.append(i)
                distance[i] = distance[cur] + 1
    for d in distance:
        if d == max(distance):
            answer += 1

    return answer
```

사용 개념

- queue 사용
- BFS 사용
- graph 구조 배열 선언 (1차원)
- for _ 사용 가능
---

---

실패 코드

```
def solution(n, edge):
    answer = 0
    distance = [-1] * n
    distance[0] = 0
    tmp = [0]
    graph = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        graph[i][i] = 1
    for i in edge:
        graph[i[0]-1][i[1]-1] = 1
        graph[i[1]-1][i[0]-1] = 1
    while tmp:
        cur = tmp.pop(0)
        for i in range(len(graph[cur])):
            if graph[cur][i] == 1:
                if distance[i] == -1:
                    tmp.append(i)
                    distance[i] = distance[cur] + 1
    for d in distance:
        if d == max(distance):
            answer += 1

    return answer
```

실패 원인
- 시간 초과로 인한 실패
- grpah 관계 구조를 2차원 배열로 풀로 선언하는 것이 문제
- 일차원 배열로 연결된 노드들만 확인
- 일차원 배열로 check 확인
- n^2에서 n으로 줄일 수 있음

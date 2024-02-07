### 여행 경로

---

성공 코드

```
from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)

    for (start, end) in tickets:
        graph[start].append(end)

    for airport in graph:
        graph[airport].sort(reverse=True)

    path = []
    stack = ["ICN"]
    while stack:
        route = stack[-1]
        if not graph[route]:
            path.append(stack.pop())
        else:
            next_route = graph[route].pop()
            stack.append(next_route)

    return path[::-1]
```

회고

- BFS풀이는 실패.. DFS로 풀어야함
- 예외처리에 관한 내용의 서술 부족
- 테스트케이스 불통..
- BFS/DFS특징을 잘 알아 놔야 할듯

---

실패 코드

```
def solution(tickets):
    answer = ["ICN"]
    dic = {}
    queue = ["ICN"]
    for i in tickets:
        if not i[0] in dic:
            dic[i[0]] = [i[1]]
            continue
        dic[i[0]].append(i[1])
    for i in dic.values():
        i.sort()
    while queue:
        cur = queue.pop(0)
        if dic[cur]:
            for i in range(len(dic[cur])):
                if dic[cur][i] in dic:
                    queue.append(dic[cur][i])
                    answer.append(dic[cur][i])
                    dic[cur].pop(i)
                    break
    if dic[cur]:
        answer.append(dic[cur][0])
    return answer

```

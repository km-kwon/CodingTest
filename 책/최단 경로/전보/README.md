### 전보

성공 코드

```
from collections import deque
import heapq
INF = int(1e9)


def solution():
    node, edge, start = map(int, input().split(" "))
    graph = [[]for i in range(node+1)]
    distance = [INF] * (node+1)

    for _ in range(edge):
        x, y, z = map(int, input().split())
        graph[x].append((y, z))

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue

            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
    dijkstra(start)
    count = 0
    max_distance = 0
    for d in distance:
        if d != INF:
            count += 1
            max_distance = max(max_distance, d)
    print(count-1, max_distance)
    return 0


solution()

```

사용 개념

- 다익스트라 알고리즘

---

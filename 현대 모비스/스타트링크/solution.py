from collections import deque

F, S, G, U, D = map(int, input().split())
queue = deque()
arr = [1e9] * F
arr[S - 1] = 0
queue.append(S - 1)
visit = [False] * F
while queue:
    cur = queue.popleft()
    next_up = cur + U
    next_down = cur - D
    if next_up < F and visit[next_up] == False:
        arr[next_up] = arr[cur] + 1
        queue.append(next_up)
        visit[next_up] = True
    if next_down >= 0 and visit[next_down] == False:
        arr[next_down] = arr[cur] + 1
        queue.append(next_down)
        visit[next_down] = True

arr[S - 1] = 1
if arr[G - 1] == 1e9:
    print("use the stairs")
else:
    print(arr[G - 1])

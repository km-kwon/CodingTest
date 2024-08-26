from collections import deque


def solution():
    n, m = map(int, input().split())
    arr = []
    visit = [-1] * n
    for i in range(n):
        temp_arr = list(map(int, input().split()))
        arr.append(temp_arr)
    plan = list(map(int, input().split()))
    heap = deque()
    heap.append(plan[0]-1)
    while heap:
        cur = heap.popleft()
        visit[cur] = 1
        for i in range(len(arr[cur])):
            if arr[cur][i] == 1 and visit[i] == -1:
                heap.append(i)
    for i in plan:
        if visit[i-1] == -1:
            print("NO")
            return
    print("YES")
    return


solution()

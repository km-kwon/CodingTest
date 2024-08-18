from collections import deque


def roadCount(start, end, arr, node):
    queue = deque()
    queue.append(start)
    distance = [-1]*node
    distance[start-1] = 0
    while queue:
        cur = queue.popleft()
        for i in range(len(arr[cur-1])):
            if arr[cur-1][i] == 1 and distance[i] == -1:
                distance[i] = distance[cur-1]+1
                queue.append(i+1)
    return distance[end-1]


def solution():
    node, edge = map(int, input().split(" "))
    arr = [[0]*(node) for _ in range(node)]
    for i in range(edge):
        node_1, node_2 = map(int, input().split(" "))
        arr[node_1-1][node_2-1] = 1
        arr[node_2-1][node_1-1] = 1

    X, K = map(int, input().split(" "))

    first = roadCount(1, K, arr, node)
    second = roadCount(K, X, arr, node)
    if first == -1 or second == -1:
        print(-1)
    else:
        print(first+second)
    return 0


solution()

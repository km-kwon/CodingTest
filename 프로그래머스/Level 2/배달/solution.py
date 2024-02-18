from collections import deque


def solution(N, road, K):
    answer = 0
    dic = [[] for _ in range(N+1)]
    for i in road:
        dic[i[0]].append([i[1], i[2]])
        dic[i[1]].append([i[0], i[2]])
    check = [-1] * (N+1)
    check[1] = 0
    que = deque()
    que.append(1)
    while que:
        cur = que.popleft()
        for node, dist in dic[cur]:
            if check[node] == -1 or (check[node] > check[cur] + dist):
                check[node] = check[cur] + dist
                que.append(node)
    for i in range(1, N+1):
        if check[i] <= K:
            answer += 1
    return answer


solution(5,	[[1, 2, 1], [2, 3, 3], [5, 2, 2],
             [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3)
solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [
    3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4)


'''
from collections import deque


def solution(N, road, K):
    answer = 0
    dic = [[] for _ in range(N)]
    for i in road:
        dic[i[0]-1].append([i[1]-1, i[2]])
        dic[i[1]-1].append([i[0]-1, i[2]])
    check = [-1] * N
    check[0] = 0
    que = deque()
    que.append(0)
    while que:
        cur = que.popleft()
        for i in dic[cur]:
            if check[i[0]] == -1:
                check[i[0]] = check[cur] + i[1]
                que.append(i[0])
            if check[i[0]] > check[cur] + i[1]:
                check[i[0]] = check[cur] + i[1]
    for i in check:
        if i <= K:
            answer += 1
    return answer

'''

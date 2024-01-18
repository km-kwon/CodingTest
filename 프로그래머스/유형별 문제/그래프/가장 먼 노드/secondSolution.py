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


solution(6,	[[1, 2], [1, 3], [2, 4], [3, 2], [3, 6], [4, 3], [5, 2]])


'''def solution(n, edge):
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

'''

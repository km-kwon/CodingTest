
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])  # 비용을 기준으로 오름차순 정렬
    connect = set([costs[0][0]])  # 간선 연결 정보를 담는 set
    while len(connect) != n:
        for cost in costs:
            if cost[0] in connect and cost[1] in connect:  # 사이클 형성을 막음
                continue
            if cost[0] in connect or cost[1] in connect:  # 기존 간선과 이어져야 함
                connect.update([cost[0], cost[1]])
                answer += cost[2]
                break

    return answer


solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])


'''def solution(n, costs):
    cost = [-1]*n
    cost[0] = 0
    road = [[] for i in range(n)]
    costs.sort()
    for i in costs:
        road[i[0]].append([i[1], i[2]])
        road[i[1]].append([i[0], i[2]])
    for i in road:
        for j in i:
            if cost[j[0]] == -1:
                cost[j[0]] = j[1]
                continue
            cost[j[0]] = min(cost[j[0]], j[1])
    return sum(cost)

'''

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


# solution(3, [[1, 2], [2, 3]], [2, 3],	1)
solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]],	[1, 3, 5],	5)

'''
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
'''

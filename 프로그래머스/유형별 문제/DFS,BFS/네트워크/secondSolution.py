def solution(n, computers):
    answer = 0
    check = [0] * n
    for node in range(len(check)):
        if check[node] == 1:
            continue
        tmp = []
        tmp.append(node)
        check[node] = 1
        while tmp:
            cur = tmp.pop(0)
            for next in range(len(computers[cur])):
                if check[next] == 0:
                    if computers[cur][next] == 1:
                        tmp.append(next)
                        check[next] = 1
        answer += 1
    return answer


solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])

def solution(routes):
    answer = 1
    routes = sorted(routes, key=lambda x: x[1])
    cur_position = routes[0][1]
    for i in routes:
        if cur_position >= i[0] and cur_position <= i[1]:
            continue
        cur_position = i[1]
        answer += 1
    return answer


solution([[-20, -15], [-18, -13], [-5, -3], [-14, -5]])

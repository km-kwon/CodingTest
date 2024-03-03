def solution(targets):
    answer = 1
    targets.sort(key=lambda x: x[1])
    cur = targets[0][1]
    for i in targets:
        if cur > i[0] and cur <= i[1]:
            continue
        else:
            answer += 1
            cur = i[1]
    return answer

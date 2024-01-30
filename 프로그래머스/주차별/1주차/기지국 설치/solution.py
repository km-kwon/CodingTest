def solution(n, stations, w):
    answer = 0
    check = []
    can_check = 2*w + 1
    for i in stations:
        start = max(0, i - 1 - w)
        end = min(n - 1, i - 1 + w)
        check.append([start, end])
    cur = -1
    for i in check:
        length = i[0] - cur - 1
        if length % can_check == 0:
            answer += length/can_check
            cur = i[1]
            continue
        answer += length//can_check + 1
        cur = i[1]
    if cur != n-1:
        length = n-1 - cur
        if length % can_check == 0:
            answer += length/can_check
            cur = i[1]
        else:
            answer += length//can_check + 1
            cur = i[1]
    return int(answer)


solution(11, [4, 11], 1)
solution(16,	[9], 2)


'''
def solution(n, stations, w):
    answer = 0
    check = [0]*n 
    for i in stations:
        for j in range(-w, w+1):
            if i-1+j < 0:
                continue
            try:
                check[i-1+j] = 1
            except IndexError:
                continue
    cur = 0
    while cur < n:
        if check[cur] == 0:
            answer += 1
            cur += ((2*w)+1)
            continue
        cur += 1
    return answer

'''

def solution(n, s):
    answer = []
    while n > 0:
        if s < n:
            answer.append(-1)
            break
        val = int(s/n)
        s = s - val
        n = n-1
        answer.append(val)
    return answer

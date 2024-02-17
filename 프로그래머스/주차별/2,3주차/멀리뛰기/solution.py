def solution(n):
    answer = [0] * (n+1)

    if n < 3:
        return n
    answer[1] = 1
    answer[2] = 2
    for i in range(3, n+1):
        answer[i] = (answer[i-1] + answer[i-2]) % 1234567
    return answer[n]


solution(1)
solution(2)
solution(3)
solution(4)
solution(5)

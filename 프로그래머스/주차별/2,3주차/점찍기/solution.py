import math


def solution(k, d):
    answer = 0
    for i in range(0, d+1, k):
        max_y = int(math.sqrt(d**2 - i**2))
        answer += (int(max_y/k)+1)
    return answer


solution(2, 4)
solution(1, 5)

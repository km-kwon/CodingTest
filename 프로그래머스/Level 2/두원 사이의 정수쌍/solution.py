import math


def solution(r1, r2):
    answer = 0

    for x in range(1, r2+1):
        y = int(math.sqrt(r2*r2 - x*x))
        if x < r1:
            y1 = math.ceil(math.sqrt(r1*r1 - x*x))
        else:
            y1 = 0
        answer = answer + y - y1+1
    return answer*4


solution(2, 3)

def find_min(nubmber, cur_position):
    value = 0
    position = 0
    return value, position


def solution(numbers):
    answer = 0
    for i in numbers:
        value_left, position = find_min()
        answer += min(value_left, position)
    return answer


solution("1756")
solution("5123")

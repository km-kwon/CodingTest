def solution(numbers, target):
    answer = 0
    result = [0]
    for i in numbers:
        tmp = []
        for j in result:
            tmp.append(j + i)
            tmp.append(j - i)
        result = tmp
    for i in result:
        if i == target:
            answer += 1
    print(answer)
    return answer


solution([1, 1, 1, 1, 1], 3)
solution([4, 1, 2, 1], 4)

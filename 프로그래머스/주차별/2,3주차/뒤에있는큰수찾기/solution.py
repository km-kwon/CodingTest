def solution(numbers):
    answer = [-1] * len(numbers)
    stack = [0]
    for i in range(1, len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
            continue
        stack.append(i)
    return answer


solution([2, 3, 3, 5])
solution([9, 1, 5, 3, 6, 2])

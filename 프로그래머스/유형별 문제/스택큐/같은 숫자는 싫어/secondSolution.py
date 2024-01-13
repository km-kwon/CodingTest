def solution(arr):
    answer = []
    cur = 0
    answer.append(arr[0])
    for i in range(0, len(arr)):
        if answer[cur] != arr[i]:
            answer.append(arr[i])
            cur += 1
    print(answer)
    return answer


solution([4, 4, 4, 3, 3])
solution([1, 1, 3, 3, 0, 1, 1])

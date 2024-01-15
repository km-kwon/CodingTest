def solution(answers):
    answer = []
    per1 = [1, 2, 3, 4, 5]
    per2 = [2, 1, 2, 3, 2, 4, 2, 5]
    per3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == per1[i % 5]:
            count[0] += 1
        if answers[i] == per2[i % 8]:
            count[1] += 1
        if answers[i] == per3[i % 10]:
            count[2] += 1
    winner = max(count)
    for i in range(len(count)):
        if count[i] == winner:
            answer.append(i+1)
    return answer


solution([1, 2, 3, 4, 5])
solution([1, 3, 2, 4, 2])

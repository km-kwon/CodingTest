def solution(triangle):
    answer = [[] for i in triangle]
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            answer[i].append(0)
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            if i == 0 and j == 0:
                answer[i][j] = triangle[i][j]
                continue
            if j == 0:
                answer[i][j] = answer[i-1][j] + triangle[i][j]
                continue
            if j == len(triangle[i])-1:
                answer[i][j] = answer[i-1][j-1] + triangle[i][j]
                continue
            answer[i][j] = max((answer[i-1][j-1]),
                               (answer[i-1][j])) + triangle[i][j]
    return max(answer[-1])


solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])

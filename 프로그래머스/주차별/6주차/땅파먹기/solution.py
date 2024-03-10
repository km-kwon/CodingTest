def solution(land):
    answer = 0
    for i in range(1, len(land)):
        for j in range(len(land[i])):
            cur = land[i][j]
            for k in range(len(land[i-1])):
                if j == k:
                    continue
                if (cur + land[i-1][k]) > land[i][j]:
                    land[i][j] = cur + land[i-1][k]
    return max(land[i])

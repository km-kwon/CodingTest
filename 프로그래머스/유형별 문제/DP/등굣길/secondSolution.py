def solution(m, n, puddles):
    arr = [[0 for j in range(m+1)] for i in range(n+1)]
    arr[1][1] = 1
    for i in puddles:
        arr[i[1]][i[0]] = -1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if arr[i][j] == -1:
                arr[i][j] = 0
                continue
            arr[i][j] = arr[i][j-1] + arr[i-1][j]
    return arr[n][m] % 1000000007


solution(4,	3,	[[2, 2]])

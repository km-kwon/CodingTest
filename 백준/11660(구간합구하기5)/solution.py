from collections import deque


def solution():
    n, m = map(int, input().split())
    arr = [[0] * (n+1)]
    sum = [[0] * (n+1) for _ in range(n+1)]
    result = []
    for i in range(1, n+1):
        temp = list(map(int, input().split()))
        arr.append([0] + temp)

    for i in range(1, len(sum)):
        for j in range(1, len(sum[0])):
            sum[i][j] = sum[i-1][j] + sum[i][j-1] + arr[i][j] - sum[i-1][j-1]
    for i in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        count = sum[x2][y2] - (sum[x1-1][y2] + sum[x2][y1-1]) + sum[x1-1][y1-1]
        result.append(count)
    for i in result:
        print(i)
    return 0


solution()

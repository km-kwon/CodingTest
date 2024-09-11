import copy


def spread(arr, row, col):
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    afterSpread = [[0]*col for _ in range(row)]
    for y in range(row):
        for x in range(col):
            if arr[y][x] == -1:
                afterSpread[y][x] = -1
            elif arr[y][x] != 0 and arr[y][x] != -1:
                spreadValue = arr[y][x] // 5
                count = 0
                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if nx >= 0 and nx < col and ny >= 0 and ny < row and arr[ny][nx] != -1:
                        count += 1
                        afterSpread[ny][nx] += spreadValue
                afterSpread[y][x] += (arr[y][x] - (spreadValue*count))
    arr = afterSpread
    return


def cleaning(arr, air, row, col):
    #

    return


def solution():

    row, col, time = map(int, input().split())
    arr = []
    air = []
    for i in range(row):
        temp = list(map(int, input().split()))
        arr.append(temp)
    for i in range(row):
        if arr[i][0] == -1:
            air.append(i)
    for i in range(time):
        spread(arr, row, col)
        cleaning(arr, air, row, col)

    return


solution()

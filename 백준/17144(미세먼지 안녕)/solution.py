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
    return afterSpread


def cleaning(arr, air, row, col):
    temp = copy.deepcopy(arr)
    for i in range(2,col):
        arr[air[0]][i] = temp[air[0]][i-1]
    for i in range(0,air[0]):
        arr[i][col-1] = temp[i+1][col-1]
    for i in range(0,col-1):
        arr[0][i] = temp[0][i+1]
    for i in range(1,air[0]):
        arr[i][0] = temp[i-1][0]

    for i in range(2, col):
        arr[air[1]][i] = temp[air[1]][i-1]
    for i in range(air[1]+1, row):
        arr[i][col-1] = temp[i-1][col-1]
    for i in range(0,col-1):
        arr[row-1][i] = temp[row-1][i+1]
    for i in range(air[1]+1, row-1):
        arr[i][0] = temp[i+1][0]
    arr[air[1]][1] = 0
    arr[air[0]][1] = 0
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
        arr = spread(arr, row, col)
        cleaning(arr, air, row, col)
    count = 0 
    for i in range(row):
        for j in range(col):
            if arr[i][j] != -1 and arr[i][j] != 0:
                count+= arr[i][j]
    print(count)
    return


solution()

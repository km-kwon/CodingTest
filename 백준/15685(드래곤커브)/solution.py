from collections import deque
import copy
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def check(arr, x, y, dir, g):

    dots = deque()
    arr[y][x] = 1
    arr[y + dy[dir]][x + dx[dir]] = 1
    dots.appendleft((x, y))
    dots.appendleft((x + dx[dir], y + dy[dir]))
    for i in range(g):
        curX, curY = dots[0]
        tempDots = copy.deepcopy(dots)
        for j in range(1, len(tempDots)):
            tempDir = [tempDots[j][0]-tempDots[j-1]
                       [0], tempDots[j][1]-tempDots[j-1][1]]
            # 이전에서 지금이 위
            if tempDir[0] == 0 and tempDir[1] == -1:
                curX += 1
            # 오른쪽
            elif tempDir[0] == 1 and tempDir[1] == 0:
                curY += 1
            # 아래
            elif tempDir[0] == 0 and tempDir[1] == 1:
                curX -= 1
            # 왼쪽
            elif tempDir[0] == -1 and tempDir[1] == 0:
                curY -= 1
            arr[curY][curX] = 1
            dots.appendleft((curX, curY))
    return


def solution():
    n = int(input())
    count = 0
    arr = [[0]*101 for _ in range(101)]
    for i in range(n):
        x, y, dir, g = map(int, input().split())
        check(arr, x, y, dir, g)
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 1 and arr[i+1][j] == 1 and arr[i][j+1] == 1 and arr[i+1][j+1] == 1:
                count += 1
    print(count)
    return


solution()

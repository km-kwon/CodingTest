from collections import deque


def solution(maps):
    answer = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x = len(maps[0])
    y = len(maps)
    check = [[-1]*x for _ in range(y)]
    check[0][0] = 1
    que = deque()
    que.append((0, 0, 1))
    while que:
        cy, cx, road = que.popleft()
        for i in range(4):
            move_y = cy + dy[i]
            move_x = cx + dx[i]
            if 0 <= move_y <= y-1 and 0 <= move_x <= x-1 and check[move_y][move_x] == -1 and maps[move_y][move_x] == 1:
                check[move_y][move_x] == road + 1
                que.append((move_y, move_x, road+1))

    return check[y-1][x-1]


solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
         1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]])

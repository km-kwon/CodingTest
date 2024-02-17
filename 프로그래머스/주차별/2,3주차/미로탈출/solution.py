from collections import deque


def bfs(start, end, maps):
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    n = len(maps)  # 세로 길이
    m = len(maps[0])  # 가로 길이
    visited = [[False]*m for _ in range(n)]
    que = deque()
    flag = False

    for i in range(n):
        for j in range(m):
            if maps[i][j] == start:
                que.append((i, j, 0))
                visited[i][j] = True
                flag = True
                break
        if flag:
            break

    while que:
        y, x, cost = que.popleft()

        if maps[y][x] == end:
            return cost

        for i in range(4):
            move_y = y+dy[i]
            move_x = x+dx[i]

            if 0 <= move_y < n and 0 <= move_x < m and maps[move_y][move_x] != "X":
                if not visited[move_y][move_x]:
                    que.append((move_y, move_x, cost+1))
                    visited[move_y][move_x] = True
    return -1


def solution(maps):
    path1 = bfs("S", "L", maps)
    path2 = bfs("L", "E", maps)
    if path1 != -1 and path2 != -1:
        return path1+path2
    return -1


solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"])
solution(["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"])

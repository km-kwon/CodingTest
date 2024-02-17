from collections import deque


def solution(maps):
    answer = []
    n, m = len(maps), len(maps[0])  # n은 세로 m은 가로의 길이
    que = deque()
    visited = [[False]*m for _ in range(n)]
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    var = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "X" or visited[i][j] == True:
                continue
            if visited[i][j] == False:
                visited[i][j] = True
                que.append((i, j, var))
                answer.append(int(maps[i][j]))
                var += 1
            while que:
                cur_y, cur_x, cur_var = que.popleft()
                for k in range(4):
                    if 0 <= cur_y+dy[k] < n and 0 <= cur_x+dx[k] < m and maps[cur_y+dy[k]][cur_x+dx[k]] != "X" and visited[cur_y+dy[k]][cur_x+dx[k]] == False:
                        que.append((cur_y+dy[k], cur_x+dx[k], cur_var))
                        visited[cur_y+dy[k]][cur_x+dx[k]] = True
                        answer[cur_var] += int(maps[cur_y+dy[k]][cur_x+dx[k]])
    if answer:
        answer.sort()
        print(answer)
    return [-1]


solution(["XXX", "XXX", "XXX"])
solution(["X591X", "X1X5X", "X231X", "1XXX1"])

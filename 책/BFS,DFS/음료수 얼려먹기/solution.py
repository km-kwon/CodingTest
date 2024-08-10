def solution():
    # dir은 멋대로 제시해 주는것이 아니다.
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    # n은 세로 m은 가로
    n, m = map(int, input().split(' '))
    visited = [[0]*m for _ in range(n)]
    cur_y, cur_x, dir = map(int, input().split(' '))
    visited[cur_y][cur_x] = 1

    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split(' '))))

    count = 1
    turn_time = 0
    while True:
        if dir == 0:
            dir = 3
        else:
            dir -= 1

        # 한번 돌았으
        turn_time += 1
        next_x = cur_x + dx[dir]
        next_y = cur_y + dy[dir]
        # 바라보는 방향이 육지이고 안가보면 가는걸로
        if visited[next_y][next_x] == 0 and arr[next_y][next_x] == 0:
            visited[next_y][next_x] = 1
            cur_y = next_y
            cur_x = next_x
            count += 1
            turn_time = 0
            continue

        # 바라보는 방향이 못가는 경우
        if turn_time == 4:
            next_x = cur_x - dx[dir]
            next_y = cur_y - dy[dir]
            if arr[next_y][next_x] == 0:
                cur_x = next_x
                cur_y = next_y
            else:
                break
            turn_time = 0
    print(count)
    return 0


solution()

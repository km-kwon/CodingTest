from collections import deque

def solution():
    # dir은 멋대로 제시해 주는것이 아니다.
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    queue= deque()
    queue.append((0,0))
    height, width = map(int, input().split())
    visited = [[0]*width for _ in range(height)]
    visited[0][0] = 1
    
    arr = []
    for i in range(height):
        arr.append(list(map(int, input())))

    while queue:
        cur_y, cur_x = queue.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if next_x<0 or next_x>=width or next_y < 0 or next_y>=height:
                continue
            if visited[next_y][next_x] == 0 and arr[next_y][next_x] == 1:
                if (next_y,next_x) not in queue:
                    queue.append((next_y,next_x))
                    visited[next_y][next_x] = visited[cur_y][cur_x] + 1
            elif visited[next_y][next_x] != 0 and  arr[next_y][next_x] == 1 and ((visited[cur_y][cur_x] + 1)<visited[next_y][next_x]):
                if (next_y,next_x) not in queue:
                    queue.append((next_y,next_x))
                    visited[next_y][next_x] = visited[cur_y][cur_x] + 1
    print(visited[height-1][width-1])       
    return 0


solution()

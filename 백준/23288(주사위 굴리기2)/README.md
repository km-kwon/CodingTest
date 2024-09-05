### 주사위 굴리기 2

성공 코드

```
from collections import deque

def east_roll(arr):
    temp  = arr[1][0]
    arr[1][0] = arr[3][1]
    arr[3][1] = arr[1][2]
    arr[1][2] = arr[1][1]
    arr[1][1] = temp
    return
def west_roll(arr):
    temp  = arr[1][0]
    arr[1][0] = arr[1][1]
    arr[1][1] = arr[1][2]
    arr[1][2] = arr[3][1]
    arr[3][1] = temp
    return
def north_roll(arr):
    temp  = arr[0][1]
    arr[0][1] = arr[1][1]
    arr[1][1] = arr[2][1]
    arr[2][1] = arr[3][1]
    arr[3][1] = temp
    return
def south_roll(arr):
    temp  = arr[0][1]
    arr[0][1] = arr[3][1]
    arr[3][1] = arr[2][1]
    arr[2][1] = arr[1][1]
    arr[1][1] = temp
    return

def solution():
    dice = [[-1,2,-1],[4,1,3],[-1,5,-1],[-1,6,-1]]
    n,m,k = map(int,input().split())
    table = []
    for i in range(n):
        temp_arr = list(map(int,input().split()))
        table.append(temp_arr)

    #방향 선언
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    cur_y,cur_x = 0,0
    # 0,1,2,3 각각 북 동 남 서
    cur_dir = 1
    score = 0
    for i in range(k):
        #다음칸 진행 가능 여부에 따른 방향 체크
        if cur_y + dy[cur_dir] < 0 or cur_y+dy[cur_dir] >= n or cur_x+dx[cur_dir] < 0 or cur_x+dx[cur_dir] >= m:
            cur_dir = (cur_dir+2)%4
        # 다음칸으로 주사위 이동
        cur_y = cur_y + dy[cur_dir]
        cur_x = cur_x + dx[cur_dir]
        # 주사위 이동시 굴림
        if cur_dir == 0:
            north_roll(dice)
        elif cur_dir == 1:
            east_roll(dice)
        elif cur_dir==2:
            south_roll(dice)
        elif cur_dir==3:
            west_roll(dice)
        # 이동 후 위치에서 BFS
        visited = [[-1]*m for _ in range(n)]
        visited[cur_y][cur_x] = 1
        queue = deque()
        queue.append((cur_y, cur_x))
        # 이동 가능 한 위치 수 파악
        count = 1
        while queue:
            cur_bfs_y, cur_bfs_x = queue.popleft()
            visited[cur_bfs_y][cur_bfs_x] = 1
            #상하좌우 확인
            for j in range(4):
                next_bfs_y = cur_bfs_y + dy[j]
                next_bfs_x = cur_bfs_x + dx[j]
                if not ((next_bfs_y,next_bfs_x) in queue) and next_bfs_y >= 0 and next_bfs_y < n and next_bfs_x >= 0 and next_bfs_x < m and table[next_bfs_y][next_bfs_x] == table[cur_bfs_y][cur_bfs_x] and visited[next_bfs_y][next_bfs_x] == -1:
                    count += 1
                    queue.append((next_bfs_y, next_bfs_x))

        score += count * table[cur_y][cur_x]
        if dice[3][1] > table[cur_y][cur_x]:
            cur_dir = (cur_dir + 1) % 4
        elif dice[3][1] < table[cur_y][cur_x]:
            cur_dir = cur_dir - 1
            if cur_dir == -1:
                cur_dir = 3

    print(score)

    return 0


solution()

```

# 사용 개념

-   BFS, 빡구현
-   여러 상황에서 좌표를 헷갈리지 않아야함

---

# 새겨놔야 할점

-   난이도는 평이한데 문제 이해하는데 어려움을 느낌
-   예제를 잘 보고 문제를 정확히 파악하고 생각을 좀만 하면 될듯

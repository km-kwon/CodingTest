from collections import deque

# 맵의 크기 : NxN
n = int(input())
grid = [list(input()) for _ in range(n)]
q = int(input())
query = [list(map(int, input().split())) for _ in range(q)]
dir = [(-1,0),(0,1),(1,0),(0,-1)]

for r1,c1,r2,c2 in query:
    # 시작 위치 선언
    r1,c1,r2,c2 = r1-1,c1-1,r2-1,c2-1
    # 처음 거리는 최대, 시간
    time_and_jump = [[{
        1: 1e9,
        2: 1e9,
        3: 1e9,
        4: 1e9,
        5: 1e9,
    }]*n for _ in range(n)]
    # 초기 좌표값 설정  
    time_and_jump[r1][c1] = {
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
    }
    for i in range(n):
        for j in range(n):
            if grid[i][j] != '.':
                time_and_jump[i][j] = 0
    
    # 큐의 정보 = (row, col, 현재 점프력)
    queue = deque([(r1,c1,1)])

            # 현재 위치,점프력, 현재까지 걸린 시간 
    def jump(cr, cc, jump, cur_time):
        # 각 방향으로 점프
        for dr,dc in dir:
            possible = True
            nr = cr + (dr * jump)
            nc = cc + (dc * jump)
            # 범위 넘어가는지 확인, 그곳이 안전한 돌이면서, 현재까지의 시간+1이 도착보다 작으면(즉 업데이트가 된다면)
            if 0<=nr<n and 0<=nc<n and grid[nr][nc] == "." and (cur_time+1) < time_and_jump[nr][nc][jump]:
                # 착지하는 곳까지 천적 있는지 확인
                for i in range(1, jump+1):
                    tr, tc = cr+(dr*i), cc+(dc*i)
                    if grid[tr][tc] == '#':
                        possible = False
                        break
                if possible:
                    time_and_jump[nr][nc][jump] = cur_time+1
                    if not (nr,nc,jump) in queue:
                        queue.append((nr,nc,jump))
        return 

    while queue:
        cr,cc,cur_jump = queue.popleft()
        # 점프하는건 나중에 => 지금 상황에서 가능한 점프력들 모두 계산하고 각각에 대해서 하는게 나을듯
        # 1. 점프력 증가후 점프 => 각 방향에 대해서 next_jump^2 만큼 더해주고 점프
        # 점프력이 늘어날때마다 제곱씩 더해줘야함.
        cur_time = time_and_jump[cr][cc][cur_jump]

        jump(cr,cc, cur_jump, cur_time)

        up_time = cur_time
        down_time = cur_time + 1
        for up_jump in range(cur_jump+1,6):
            up_time += up_jump ** 2
            jump(cr,cc, up_jump, up_time)
        for down_jump in range(cur_jump-1, 0, -1):
            jump(cr,cc,down_jump, down_time)
    
    if time_and_jump[r2][c2] == 1e9:
        print(-1)
    else:
        print(time_and_jump[r2][c2])

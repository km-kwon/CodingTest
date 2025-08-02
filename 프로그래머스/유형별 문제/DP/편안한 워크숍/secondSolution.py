n, k = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
dr = [-1,0,1,0]
dc = [0,1,0,-1]
route = [[{1:0} for _ in range(n)] for _ in range(n)]
for count in range(1, k):
    for i in range(n):
        for j in range(n):
            for dir in range(4):
                pr = i + dr[dir]
                pc = j + dc[dir]
                if 0<=pr<n and 0<=pc<n and arr[i][j] > arr[pr][pc]:
                    if count in route[pr][pc]:
                        if not count+1 in route[i][j]:
                            route[i][j][count+1] = max(arr[i][j]-arr[pr][pc], route[pr][pc][count])
                        else:
                            if route[pr][pc][count] == 0:
                                route[i][j][count+1] = min(arr[i][j]-arr[pr][pc], route[i][j][count+1])
                            else:
                                if route[i][j][count+1] > route[pr][pc][count] and  route[i][j][count+1]>arr[i][j]-arr[pr][pc]:
                                    route[i][j][count+1] = max(arr[i][j]-arr[pr][pc], route[pr][pc][count])                
min_value = 1e9
for i in range(n):
    for j in range(n):
        if k in route[i][j]:
            min_value = min(route[i][j][k], min_value)
if min_value == 1e9:
    print(-1)
else: 
    print(min_value)
""" 
route = [[[]] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        min_dif = 1e9
        temp = []
        for dir in range(4):
            nr = i + dr[dir]
            nc = j + dc[dir]
            if 0<=nr<n and 0<=nc<n and arr[i][j] < arr[nr][nc]:
                temp.append((nr,nc,arr[nr][nc]-arr[i][j]))
        route[i][j] = temp
# 현재까지 최대값
max_value = 1e9
for i in range(n):
    for j in range(n):
        if len(route[i][j]) > 0:
            # 루트 탐색
            # 이 등산로의 높이차의 최대값
            queue = deque()
            queue.append((i,j, 1, -1))
            while queue:
                ## 현재 row, 현재 col, 나까지 포함 갯수, 나까지 오는데 최대 높이
                cr,cc,cur_count, cur_max_height = queue.pop() 
                if cur_count <= k:
                    if cur_count == k:
                        max_value = min(cur_max_height, max_value)
                        continue
                    # 다음 위치, 다음꺼까지 가는데 높이차이
                    for nr,nc,next_dif in route[cr][cc]:
                        if next_dif < max_value:
                            queue.append((nr,nc, cur_count+1,max(cur_max_height,next_dif)))
                    
if max_value == 1e9:
    print(-1)
else: 
    print(max_value) """
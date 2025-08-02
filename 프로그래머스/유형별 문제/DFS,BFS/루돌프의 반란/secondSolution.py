from collections import deque

n, m, p, c, d = map(int,input().split())
# 상 상우 우 우하 하 하좌 좌 좌상 총 8개
# 반대 방향은 +4 % 8
RUDOL_DIR = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
# 반대방향은 +2 % 4
SANTA_DIR = [(-1,0), (0,1), (1,0), (0,-1)]
RUDOL_ID = -1
# 루돌프의 위치
arr = [[0]*n for _ in range(n)]

result = {}
rudol_r, rudol_c = map(int,input().split())
rudol_r, rudol_c = rudol_r-1, rudol_c-1
arr[rudol_r][rudol_c] = RUDOL_ID

# 산타의 위치들
# [row, col, score, stun_time]
santa = {}
for _ in range(p):
    id, start_r, start_c = map(int,input().split())
    santa[id] = [start_r-1, start_c-1, 0, 0]
    arr[start_r-1][start_c-1] = id
# santa = sorted(santa.items(), key = lambda x: x[0])

def find_distance (r1,c1, r2,c2):
    return (r1-r2)**2 + (c1-c2)**2




delete_santa_info = []
# 루돌프로 인해 산타 밀려요
def hit_santa_by_rudol(cr, cc, dir, id, distance):
    global delete_santa_info
    nr, nc = cr+(RUDOL_DIR[dir][0] * distance), cc+(RUDOL_DIR[dir][1]*distance)
    if 0<=nr<n and 0<=nc<n:
        # 밀린위치에 산타가 있음
        if arr[nr][nc] != 0:
            hitted_santa_id = arr[nr][nc]
            hit_santa_by_rudol(nr,nc,dir,hitted_santa_id,1)
        arr[nr][nc] = id
        arr[cr][cc] = 0
        # 이동후 해당 산타 위치
        santa[id][0] = nr
        santa[id][1] = nc
    else:
        delete_santa_info.append(id)
    return 

# 산타로 인해 산타로 밀림
def hit_santa_by_santa(cr, cc, dir, id, distance):
    global delete_santa_info
    nr, nc = cr+(SANTA_DIR[dir][0] * distance), cc+(SANTA_DIR[dir][1]*distance)
    if 0<=nr<n and 0<=nc<n:
        # 밀린위치에 산타가 있음
        if arr[nr][nc] != 0:
            hitted_santa_id = arr[nr][nc]
            hit_santa_by_santa(nr,nc,dir,hitted_santa_id,1)
        arr[nr][nc] = id
        arr[cr][cc] = 0
        # 이동후 해당 산타 위치
        santa[id][0] = nr
        santa[id][1] = nc
    else:
        delete_santa_info.append(id)
    return 

def do_delete_santa_info():
    global delete_santa_info,n
    for i in range(n):
        for j in range(n):
            if arr[i][j] in delete_santa_info:
                arr[i][j]=0
    for i in delete_santa_info:
        result[i] = santa[i]
        del santa[i]
    delete_santa_info = []
    return 

def move_rudol(n):
    global rudol_r, rudol_c, RUDOL_ID, c
    # 가장 가까운 산타 찾기
    distance_santa_info = []
    for values in santa.values():
    # values = [start_r, start_c, score]
        # [거리, row, col]
        distance_santa_info.append((find_distance(rudol_r, rudol_c, values[0], values[1]), values[0], values[1]))
    distance_santa_info = sorted(distance_santa_info, key= lambda x:(x[0],-x[1],-x[2]))

    close_santa_row, close_santa_col = distance_santa_info[0][1], distance_santa_info[0][2]
    
    # 루돌프가 이동하는 곳 구하기
    min_next = 1e9
    
    # 루돌프가 이동하는 방향
    move_dir = -1

    for i in range(8):
        nr,nc = rudol_r + RUDOL_DIR[i][0], rudol_c + RUDOL_DIR[i][1]
        # 범위를 넘어가면 안됨
        if 0<=nr<n and 0<=nc<n:
            next_move_distance = find_distance(nr,nc, close_santa_row, close_santa_col)
            if min_next > next_move_distance:
                min_next = next_move_distance
                move_dir = i
    
    # 이동
    nr, nc = rudol_r + RUDOL_DIR[move_dir][0], rudol_c + RUDOL_DIR[move_dir][1]

    # 만약 산타가 없다면 
    if arr[nr][nc] == 0:
        arr[rudol_r][rudol_c] = 0
        arr[nr][nc] = RUDOL_ID
        rudol_r, rudol_c = nr, nc
    else:
        hit_santa_id = arr[nr][nc]
        #스턴시간
        santa[hit_santa_id][3] = 2
        #스코어 겟겟
        santa[hit_santa_id][2] += c
        #해당 위치는 이제 루돌프꺼요
        arr[rudol_r][rudol_c] = 0
        hit_santa_by_rudol(nr, nc, move_dir, hit_santa_id, c)
        arr[nr][nc] = RUDOL_ID
        rudol_r, rudol_c = nr, nc
        # 산타 밀려요



### 이동할 수 없는 부분에 대해서 예외 처리 해야함
def move_santa(n):
    global rudol_r, rudol_c, d, RUDOL_ID
    # [row, col, score, stun_time]
    
    for id in sorted(santa.keys()):
        value = santa[id]
        cr,cc = value[0], value[1]
        if value[3] > 0:
            continue
        #이동 후 루돌프와의 거리 
        distance_rudol_info = []
        for i in range(4):
            nr, nc = cr+SANTA_DIR[i][0], cc+SANTA_DIR[i][1]
            if 0<=nr<n and 0<=nc<n and (arr[nr][nc] == 0 or arr[nr][nc] == RUDOL_ID):
                # [거리, 방향]
                distance_rudol_info.append((find_distance(rudol_r, rudol_c, nr, nc), i))
        
        # 이동할 수 있는 곳이 없다면 패스
        if len(distance_rudol_info) == 0:
            continue
        distance_rudol_info = sorted(distance_rudol_info, key= lambda x:(x[0],x[1]))
        # 방향
        move_dir = distance_rudol_info[0][1]
        nr, nc = cr+SANTA_DIR[move_dir][0], cc+SANTA_DIR[move_dir][1]

        # 이동
        # 만약 루돌프가 없다면
        if arr[nr][nc] == 0:
            arr[cr][cc] = 0
            arr[nr][nc] = id
            santa[id][0] = nr
            santa[id][1] = nc
        # 만약 루돌프가 있다면
        else:
            #스코어 겟겟
            santa[id][2] += d
            santa[id][3] = 2
            move_dir = (move_dir+2) % 4
            hit_santa_by_santa(nr, nc, move_dir, id, c)
            # 산타 밀려요
            arr[cr][cc] = 0 
    return 

for i in range(m):
    move_rudol(n)
    do_delete_santa_info()
    move_santa(n)
    do_delete_santa_info()
    for key in santa.keys():
        if santa[key][3] > 0:
            santa[key][3] -= 1 
    if len(santa) == 0:
        break
    for key in santa.keys():
        santa[key][2] += 1


final_result = {}
for key,value in santa.items():
    final_result[key] = value
for key,value in result.items():
    final_result[key] = value
final_result = sorted(final_result.items(), key = lambda x:x[0])
for i in final_result:
    print(i[1][2], end=" ")
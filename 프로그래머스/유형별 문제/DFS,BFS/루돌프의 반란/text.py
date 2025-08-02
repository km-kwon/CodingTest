from collections import deque

n, m, p, c, d = map(int,input().split())
RUDOL_DIR = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
SANTA_DIR = [(-1,0), (0,1), (1,0), (0,-1)]
RUDOL_ID = -1

arr = [[0]*n for _ in range(n)]
rudol_r, rudol_c = map(int,input().split())
rudol_r, rudol_c = rudol_r-1, rudol_c-1
arr[rudol_r][rudol_c] = RUDOL_ID

santa = {}
for _ in range(p):
    id, start_r, start_c = map(int,input().split())
    santa[id] = [start_r-1, start_c-1, 0, 0] # r, c, score, stun
    arr[start_r-1][start_c-1] = id

# [개선] 탈락한 산타를 관리할 리스트 (기존 코드의 delete_santa_info 역할)
dead_santa_ids = []

def find_distance (r1,c1, r2,c2):
    return (r1-r2)**2 + (c1-c2)**2

# [개선] 중복되는 밀어내기 함수를 하나로 통합하고 오류 수정
def push_santa(start_r, start_c, direction, push_id):
    """
    (start_r, start_c)에 있는 push_id 산타를 direction 방향으로 1칸 밀어냅니다.
    연쇄 상호작용을 처리합니다.
    """
    nr, nc = start_r + direction[0], start_c + direction[1]

    if not (0 <= nr < n and 0 <= nc < n):
        dead_santa_ids.append(push_id)
        return

    # 밀려난 곳에 다른 산타가 있으면 연쇄적으로 민다
    if arr[nr][nc] > 0:
        next_push_id = arr[nr][nc]
        push_santa(nr, nc, direction, next_push_id)
    
    # 산타 위치 업데이트
    arr[nr][nc] = push_id
    santa[push_id][0], santa[push_id][1] = nr, nc

def move_rudol():
    global rudol_r, rudol_c
    
    # 살아있는 산타만 대상으로 함
    alive_santas = {sid: s_info for sid, s_info in santa.items() if sid not in dead_santa_ids}
    if not alive_santas: return

    # 가장 가까운 산타 찾기
    targets = []
    for s_id, s_info in alive_santas.items():
        dist = find_distance(rudol_r, rudol_c, s_info[0], s_info[1])
        targets.append((dist, s_info[0], s_info[1], s_id))
    
    targets.sort(key=lambda x: (x[0], -x[1], -x[2]))
    target_id = targets[0][3]
    target_r, target_c = targets[0][1], targets[0][2]

    # 루돌프 이동 방향 결정
    best_dir_idx = -1
    min_dist = float('inf')
    for i in range(8):
        nr, nc = rudol_r + RUDOL_DIR[i][0], rudol_c + RUDOL_DIR[i][1]
        dist = find_distance(nr, nc, target_r, target_c)
        if dist < min_dist:
            min_dist = dist
            best_dir_idx = i
    
    # 루돌프 이동 및 이전 위치 정리
    arr[rudol_r][rudol_c] = 0
    rudol_r += RUDOL_DIR[best_dir_idx][0]
    rudol_c += RUDOL_DIR[best_dir_idx][1]
    
    # 충돌 처리
    if arr[rudol_r][rudol_c] > 0:
        hit_santa_id = arr[rudol_r][rudol_c]
        
        santa[hit_santa_id][2] += c
        santa[hit_santa_id][3] = 2 # 현재 턴 포함 2턴간 기절

        push_dir = RUDOL_DIR[best_dir_idx]
        push_dist = c
        
        # [수정] 밀려나는 로직을 직접 처리
        final_r, final_c = rudol_r + push_dir[0] * push_dist, rudol_c + push_dir[1] * push_dist
        
        if not (0 <= final_r < n and 0 <= final_c < n):
            dead_santa_ids.append(hit_santa_id)
        else:
            if arr[final_r][final_c] > 0:
                # 연쇄 충돌 발생 시
                push_santa(final_r, final_c, push_dir, arr[final_r][final_c])
            
            arr[final_r][final_c] = hit_santa_id
            santa[hit_santa_id][0], santa[hit_santa_id][1] = final_r, final_c

    # 루돌프가 최종 위치 차지
    arr[rudol_r][rudol_c] = RUDOL_ID

def move_santas():
    # [수정] 산타 ID 순서대로 이동
    for sid in sorted(santa.keys()):
        if sid in dead_santa_ids or santa[sid][3] > 0:
            continue

        cr, cc = santa[sid][0], santa[sid][1]
        current_dist = find_distance(cr, cc, rudol_r, rudol_c)
        best_dir_idx = -1

        # 이동 방향 탐색
        for i in range(4):
            nr, nc = cr + SANTA_DIR[i][0], cc + SANTA_DIR[i][1]
            if not (0 <= nr < n and 0 <= nc < n) or arr[nr][nc] > 0:
                continue

            dist = find_distance(nr, nc, rudol_r, rudol_c)
            if dist < current_dist:
                current_dist = dist
                best_dir_idx = i
        
        if best_dir_idx == -1: continue
        
        # 산타 이동 및 이전 위치 정리
        arr[cr][cc] = 0
        nr, nc = cr + SANTA_DIR[best_dir_idx][0], cc + SANTA_DIR[best_dir_idx][1]

        # 충돌 처리
        if arr[nr][nc] == RUDOL_ID:
            santa[sid][2] += d
            santa[sid][3] = 2
            
            # [수정] 산타의 힘 d만큼 반대 방향으로 밀려남
            push_dir = SANTA_DIR[(best_dir_idx + 2) % 4]
            push_dist = d
            
            final_r, final_c = nr + push_dir[0] * push_dist, nc + push_dir[1] * push_dist
            
            if not (0 <= final_r < n and 0 <= final_c < n):
                dead_santa_ids.append(sid)
            else:
                if arr[final_r][final_c] > 0:
                    push_santa(final_r, final_c, push_dir, arr[final_r][final_c])
                
                arr[final_r][final_c] = sid
                santa[sid][0], santa[sid][1] = final_r, final_c
        else:
            # 충돌 없이 이동 성공
            arr[nr][nc] = sid
            santa[sid][0], santa[sid][1] = nr, nc

# --- 메인 루프 ---
for _ in range(m):
    if len(dead_santa_ids) == p: break

    move_rudol()
    move_santas()

    # 턴 종료 처리
    for sid in santa:
        if sid not in dead_santa_ids:
            santa[sid][2] += 1
        if santa[sid][3] > 0:
            santa[sid][3] -= 1

# --- 결과 출력 ---
final_scores = []
for sid in sorted(santa.keys()):
    final_scores.append(str(santa[sid][2]))
print(" ".join(final_scores))
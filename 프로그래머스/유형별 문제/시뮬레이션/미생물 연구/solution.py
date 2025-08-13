from collections import deque

n,q = map(int,input().split())
arr = [[0] * n for _ in range(n)]

info = [list(map(int,input().split())) for _ in range(q)]

dir = [(-1,0), (0,1), (1,0), (0,-1)]

def check_micro_divide():
    """
    투입된 미생물의 현황을 파악하고 둘로 나뉜 미생물을 제거하는 함수.

    Returns:
        object:
            'count' (number): 미생물의 총 개수.
            'info' (list[tuple[number, number]]): 각 미생물의 위치 정보 (x, y).
    """
    # 미생물 정보 : id, 영역의 갯수(나뉘었으면 1보다 큼), 좌표들
    micro_info = {}
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 미생물이 있고, 아직 방문을 안했다면 해당 위치부터 bfs 탐색
            if arr[i][j] != 0 and not visited[i][j]:
                queue = deque([(i,j)])
                visited[i][j] = True
                if not arr[i][j] in micro_info:
                    micro_info[arr[i][j]] = {
                        "count": 1,
                        "info" : [(i,j)]
                    }
                else:
                    micro_info[arr[i][j]]["count"] += 1 
                    micro_info[arr[i][j]]["info"].append((i,j))
                while queue:
                    cr,cc = queue.popleft()
                    for dr,dc in dir:
                        nr,nc = cr+dr,cc+dc
                        if 0<=nr<n and 0<=nc<n and not visited[nr][nc] and arr[i][j] == arr[nr][nc]:
                            visited[nr][nc] = True
                            queue.append((nr,nc))
                            micro_info[arr[nr][nc]]["info"].append((nr,nc))
    delete_list = []
    for key,value in micro_info.items():
        if value["count"] > 1:
            delete_list.append(key)
            for i,j in value["info"]:
                arr[i][j] = 0
    for key in delete_list:
        del micro_info[key]
    return micro_info

def move_micro(micro_info):
    after_move = [[0]*n for _ in range(n)]
    for micro_id, value in micro_info:
        center_row, center_col = value['info'][0]
        found_spot = False  # 이동 가능한 위치를 찾았는지 확인하는 플래그
        for col in range(n):
            for row in range(n):
                # 현재 (row, col) 위치로 이동 가능한지 확인
                can_move = True
                for (cr, cc) in value['info']:
                    new_row = row + cr - center_row
                    new_col = col + cc - center_col
                    # 경계를 벗어나거나 이미 다른 미생물이 있다면 이동 불가
                    if not (0 <= new_row < n and 0 <= new_col < n and after_move[new_row][new_col] == 0):
                        can_move = False
                        break # 내부 루프를 탈출
                # 이동 가능한 위치를 찾았다면
                if can_move:
                    # after_move 배열 업데이트
                    for (cr, cc) in value['info']:
                        new_row = row + cr - center_row 
                        new_col = col + cc - center_col
                        after_move[new_row][new_col] = micro_id  
                    found_spot = True
                    break # 내부 for col 루프를 탈출
            if found_spot:
                break # 바깥쪽 for row 루프를 탈출
    return after_move


def calc_area(micro_info_dict):
    check = {}
    total = 0
    for cr in range(n):
        for cc in range(n):
            if arr[cr][cc] != 0:
                for dr,dc in dir:
                    nr,nc = cr+dr, cc+dc
                    if 0<=nr<n and 0<=nc<n and arr[nr][nc] != 0 and arr[nr][nc] != arr[cr][cc]:
                        if not(arr[nr][nc], arr[cr][cc]) in check and not(arr[cr][cc],arr[nr][nc]) in check:
                            check[(arr[cr][cc],arr[nr][nc])] = True
    for id_1, id_2 in check.keys():
        total+= len(micro_info_dict[id_1]['info']) * len(micro_info_dict[id_2]['info'])
    return total


for id in range(len(info)):
    start_col, start_row, end_col, end_row = info[id][0]-1, info[id][1]-1, info[id][2]-1, info[id][3]-1
    # 미생물 투입
    for row in range(start_row+1, end_row+1):
        for col in range(start_col+1, end_col+1):
            arr[row][col] = id+1
    #미생물 둘로 나뉘었는지 확인 및 잔여 미생물들의 정보 저장
    micro_info_dict = check_micro_divide()
    # 정렬된거
    micro_info_list = sorted(micro_info_dict.items(), key = lambda x:(-len(x[1]["info"]), x[0]))
    # 옮기기
    arr = move_micro(micro_info_list)
    print(calc_area(micro_info_dict))
    


    
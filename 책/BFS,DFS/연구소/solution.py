from collections import deque
from copy import deepcopy
def solution():
    n,k = map(int,input().split())
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    arr = []
    for i in range(n):
        temp_arr = list(map(int,input().split()))
        arr.append(temp_arr)
    s, y, x = map(int,input().split())
    for cur_time in range(s):
        for cur_virus in range(1, k+1):
            arr2 = deepcopy(arr)
            # 배열 순회 i는 y j는 x
            for i in range(n):
                for j in range(n):
                    # 해당 위치에 지금 확인하는 바이러스라면
                    if arr[i][j] == cur_virus:
                        # 상하좌우 전염 on
                        for dir in range(4):
                            nx = j + dx[dir]
                            ny = i + dy[dir]
                            if nx>=0 and nx < n and ny >=0 and ny <n and arr[ny][nx] == 0:
                                arr2[ny][nx] = cur_virus
            arr = arr2
    print(arr[y][x])

    return 0


solution()

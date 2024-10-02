from collections import deque

dx = [1,-1,0,0]
dy = [0,0,-1,1]
N,K = map(int,input().split())
arr = []

# 현재 말의 위치
loc = [0]*K
# 판의 상태
status = [[deque()]*N for _ in range(N)]

for i in range(N):
    arr.append(list(map(int,input().split())))

for i in range(K):
    r,c,dir = map(int,input().split())
    loc[i] = (r,c,dir-1)
    status[r][c].append(i)

turn = 0
while True:
    for i in range(K):
        cury = loc[i][0]
        curx = loc[i][1]
        curdir = loc[i][2]

        move = []
        flag = 0
        for j in range(status[cury][curx]):
            if j == i:
                flag = 1
            if flag == 1: 
                move.append(j)

        ny = cury + dy[curdir]
        nx = curx + dx[curdir]
        if ny < 0 or ny >=N or nx <0 or nx >= N or arr[ny][nx] == 2:
            if curdir == 0:
                curdir = 1
            elif curdir == 1:
                curdir = 0
            elif curdir ==2:
                curdir = 3
            elif curdir == 3:
                curdir = 2 
        else:
            print()

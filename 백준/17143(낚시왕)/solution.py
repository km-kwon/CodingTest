from collections import deque

dx = [0, 0, 1, -1]
dy = [-1, 1, 0 ,0]

count = 0

R,C,m = map(int,input().split())
shark = {}

for i in range(m):
    r,c,s,d,z = map(int,input().split())
    r = r-1
    c = c-1
    shark[(r,c)] = (z,s,d-1)
    # z: 사이즈 s: 속력 d-1 : 방향

for cur in range(C):
    for j in range(R):
        if (j,cur) in shark:
            count += shark[(j,cur)][0]
            del shark[(j,cur)]
            break
    temp = []
    for i,j in shark.keys():
        curx = j
        cury = i 
        curZ, curSpeed, curDir = shark[(i,j)]
        if curDir == 0 or curDir == 1:
            curSpeed = curSpeed % (2*(R-1))
        else:
            curSpeed = curSpeed% (2*(C-1))
        for k in range(curSpeed):
            if curx + dx[curDir]<0 or curx + dx[curDir]>=C or cury + dy[curDir] < 0 or cury + dy[curDir]>=R:
                if curDir == 0:
                    curDir = 1
                elif curDir == 1:
                    curDir = 0
                elif curDir == 2:
                    curDir = 3
                elif curDir == 3:
                    curDir = 2
            curx = curx + dx[curDir]
            cury = cury + dy[curDir]
        temp.append((cury,curx,curZ, curSpeed, curDir))
    afterShark = {}
    for y,x,z,speed,dir in temp:
        if not (y,x) in afterShark:
            afterShark[(y,x)] = (z,speed,dir)
        else:
            if afterShark[(y,x)][0] > z:
                continue
            else:
                afterShark[(y,x)] = (z,speed,dir)
    shark = afterShark

print(count)
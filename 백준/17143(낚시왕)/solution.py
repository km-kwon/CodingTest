from collections import deque

dx = [0, 0, 1, -1]
dy = [-1, 1, 0 ,0]

count = 0

R,C,m = map(int,input().split())
arr = [[0] * C for _ in range(R)]
shark = {}

for i in range(m):
    r,c,s,d,z = map(int,input().split())
    arr[r][c] = (z,s,d-1)
    shark[(r,c)] = (z,s,d-1)
    # z: 사이즈 s: 속력 d-1 : 방향

cur = -1
for i in range(C+1):
    cur += 1
    for j in range(R):
        if (i,j) in shark:
            count += shark[(i,j)][0]
            del shark[(i,j)]
for i,j in shark.keys:
    
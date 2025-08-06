import itertools
from collections import deque

n = 5
arr = [list(input()) for _ in range(n)]
position = []
for i in range(n):
    for j in range(n):
        position.append((i,j))
com_list = itertools.combinations(position,7)

dir = [(0,1),(0,-1),(1,0),(-1,0)]
total_count = 0
for com in com_list:
    visited = [[False]*n for _ in range(n)]
    count_y = 0
    count_s = 0
    for (i,j) in com:
        visited[i][j] = True
        if arr[i][j] == 'Y':
            count_y +=1 
        elif arr[i][j] == 'S':
            count_s +=1
    if count_s < 4:
        continue
    else:
        queue = deque([com[0]])
        visited[com[0][0]][com[0][1]] = False
        count = 1
        while queue:
            cr, cc = queue.popleft()
            for dr, dc in dir:
                nr, nc = cr+dr, cc+dc
                if 0 <= nr < n and 0 <= nc < n and visited[nr][nc]:
                    queue.append((nr,nc))
                    visited[nr][nc] = False
                    count += 1
        if count == 7:
            total_count +=1
print(total_count)
dir = [(-1,0),(0,1), (1,0), (0,-1)]
n,m = map(int,input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int,input().split())))
points = []
for _ in range(m):
    row,col = map(int,input().split())
    points.append((row-1,col-1))

visited = [[False] * n for _ in range(n)]
start_r = points[0][0]
start_c = points[0][1]
visited[start_r][start_c] = True

count = 0
def back (n,m, cr, cc, cur_index):
    global count
    if cur_index == m:
        count+=1
        return
    for i in range(cur_index+1, m):
        if visited[points[i][0]][points[i][1]]:
            return

    for dr,dc in dir:
        nr,nc = cr+dr, cc+dc
        if 0<=nr<n and 0<=nc<n and not visited[nr][nc] and grid[nr][nc] == 0:
            visited[nr][nc] = True
            if nr == points[cur_index][0] and nc == points[cur_index][1]:
                back(n,m, nr, nc, cur_index + 1)
            else:
                back(n,m,nr,nc,cur_index)
            visited[nr][nc] = False

back(n, m, points[0][0], points[0][1], 1)

print(count)
from collections import deque


dx = [0,1,0,-1]
dy = [-1,0,1,0]

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input())))

visit = [[False for _ in range(n)]for _ in range(n)]

result = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visit[i][j] == False:
            count=1
            visit[i][j] = True
            queue = deque() 
            queue.append((i,j))
            while queue:
                cy,cx = queue.popleft()
                for i in range(4):
                    ny = cy + dy[i]
                    nx = cx + dx[i]
                    if ny >= 0 and ny < n and nx >= 0 and nx < n and arr[ny][nx] == 1 and visit[ny][nx] == False:
                        queue.append((ny,nx))
                        visit[ny][nx] = True
                        count += 1
            result.append(count) 

result.sort()

print(len(result))
for i in result:
    print(i)

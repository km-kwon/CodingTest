from collections import deque
queue = deque()

dir = [(-1,0), (0,1), (1,0), (0,-1)]

len_col, len_row = map(int,input().split())
miro = []
for i in range(len_row):
    miro.append(list(map(int,input())))

# 각 칸에 도달하기까지 부숴야 하는 벽의 갯수
arr = [[1e9]*len_col for _ in range(len_row)]
arr[0][0] = 0
queue.append((0, 0))

while queue:
    cr,cc = queue.popleft()
    for i in range(4):
        nr,nc = cr+dir[i][0], cc+dir[i][1]
        if 0<=nr<len_row and 0<=nc<len_col:
            if miro[nr][nc] == 1 and arr[nr][nc] > arr[cr][cc] + 1:
                # 만약 queue에 없으면 넣어주고
                if not (nr,nc) in queue:
                    queue.append((nr,nc))
                arr[nr][nc] = arr[cr][cc] + 1
            elif miro[nr][nc] == 0 and arr[nr][nc] > arr[cr][cc]:
                if not (nr,nc) in queue:
                    queue.append((nr,nc))
                arr[nr][nc] = arr[cr][cc]

print(arr[len_row-1][len_col-1])

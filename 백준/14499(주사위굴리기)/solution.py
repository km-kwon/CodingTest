n,m,y,x,k = map(int,input().split())
dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, -1, 1]

dice = [[0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0]]

arr = []
result = []
for i in range(n):
    arr.append(list(map(int, input().split())))

def roll(x,y,dir):
    global dice
    global arr
    global result
    if dir == 1:
        temp = dice[1][2]
        dice[1][2] = dice[1][1]
        dice[1][1] = dice[1][0]
        dice[1][0] = dice[3][1]
        dice[3][1] = temp
    elif dir == 2:
        temp = dice[1][2]
        dice[1][2] = dice[3][1]
        dice[3][1] = dice[1][0]
        dice[1][0] = dice[1][1]
        dice[1][1] = temp
    elif dir == 3:
        temp = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = dice[3][1]
        dice[3][1] = temp
    elif dir == 4:
        temp = dice[0][1]
        dice[0][1] = dice[3][1]
        dice[3][1] = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = temp
    if arr[y][x] == 0:
        arr[y][x] = dice[3][1]
    else:
        dice[3][1] = arr[y][x]
        arr[y][x] = 0
    result.append(dice[1][1])
    return

command = list(map(int,input().split()))
for i in command:
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and ny >= 0 and nx < m and ny < n:
        x = nx
        y = ny 
        roll(x,y,i)
for i  in result:
    print(i)


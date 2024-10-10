from collections import deque

N,K = map(int,input().split())
temp = list(map(int,input().split()))
arr = deque()
for i in temp:
    arr.append([0,i])

count = 1

while True:
    # 로봇과 회전
    temp = arr.pop()
    arr.appendleft(temp)
    # 한칸 회전했을때 내리는 칸이면 내려
    if arr[N-1][0] == 1:
        arr[N-1][0] = 0
    #로봇 이동
    for i in range(N):
        if arr[N-1-i][0] == 1 and arr[N-i][0] ==0 and arr[N-i][1]>=1:
            arr[N-1-i][0] = 0
            arr[N-i][0] = 1
            arr[N-i][1] -=1
    if arr[N-1][0] == 1:
        arr[N-1][0] = 0
    # 로봇올려
    if arr[0][0] == 0 and arr[0][1]>=1:
        arr[0][0] = 1
        arr[0][1] -=1
    K_Count = 0
    for i in range(2*N):
        if arr[i][1] <= 0:
            K_Count+=1
    if K_Count >= K:
        break
    count+=1

print(count)
        
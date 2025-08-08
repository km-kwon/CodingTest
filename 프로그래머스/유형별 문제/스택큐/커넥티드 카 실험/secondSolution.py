from collections import deque


n, s = map(int,input().split())
init = list(map(int,input().split()))
oil = list(map(int,input().split()))

# 초기 위치 및 잔여 연료
left=0
can_left = 1e9
right=0
can_right = 0
result = []

queue = deque()

# 각 위치에 있는 자동차의 번호
arr = [[] * n for _ in range(n)]
for i in range(n):
    # 자동차 정보 = (위치, 오일, 차번호(id))
    arr[i] = (init[i]-1,oil[i],i+1)
    if i+1 == s:
        left,right= i-1,i+1
        queue.append(i)
        result.append(arr[i][2])


while queue:
    cur = queue.popleft()
    can_left = min(arr[cur][0] - arr[cur][1], can_left)
    can_right = max(arr[cur][0] + arr[cur][1], can_right)
    while right < n and can_right >= arr[right][0]:
        result.append(arr[right][2])
        queue.append(right)
        right += 1
    while  left >= 0 and can_left <= arr[left][0]:
        result.append(arr[left][2])
        queue.append(left)
        left-=1

result.sort()
print(*result)


""" 
for i in range(left-1, -1, -1):
    if can_left <= arr[i][0]:
        can_left = min(arr[i][0] - arr[i][1], can_left)
        can_right = max(arr[i][0] + arr[i][1], can_right)
        result.append(arr[i][2])
        continue
    break

for i in range(left+1,n):
    if can_right >= arr[i][0]:
        can_right = max(arr[i][0] + arr[i][1], can_right)
        can_left = min(arr[i][0] - arr[i][1], can_left)
        result.append(arr[i][2])
        continue
    break



# 잔여 연료량이 있는경우
while right[1] and right[0] < n-1:
    next_x = right[0] + 1
    if next_x < n: 
        # 다음위치일때 잔여 연료량 
        next_oil = right[1] - 1
        # 다음 위치에 자동차가 있다면
        if len(arr[next_x]) > 0:
            result.append(arr[next_x][0])
            # 거기 도착했을때 연료가 남은 연료보다 많다면
            if arr[next_x][1] > next_oil:
                next_oil = arr[next_x][1]
        right[0] = next_x
        right[1] = next_oil

while left[1] and left[0] > 0:
    next_x = left[0] - 1
    if next_x > 0: 
        # 다음위치일때 잔여 연료량 
        next_oil = left[1] - 1
        # 다음 위치에 자동차가 있다면
        if len(arr[next_x]) > 0:
            result.append(arr[next_x][0])
            # 거기 도착했을때 연료가 남은 연료보다 많다면
            if arr[next_x][1] > next_oil:
                next_oil = arr[next_x][1]
        left[0] = next_x
        left[1] = next_oil

 """



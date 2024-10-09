from collections import deque

N, M, T = map(int, input().split())
status = [deque() for _ in range(N+1)]

for i in range(1, N+1):
    temp = list(map(int, input().split()))
    for j in temp:
        status[i].append()

for i in range(T):
    x, d, k = map(int, input().split())
    # 돌려돌려 돌림판
    for j in range(1, N):
        # j가 x의 배수라면 움직여야하는 원판
        if j % x:
            # k만큼 움직이기
            if d == 0:
                for move in k:
                    temp = status[j].pop()
                    status[j].appendleft(temp)
            elif d == 1:
                for move in k:
                    temp = status[j].popleft()
                    status[j].append(temp)
    # 전체 순회 및 체크
    for j in range(1, len(status)+1):
        for num in range(M):
            if sum(status[j]) != -M:
                # 이거 약간 같은게 연속해서 주루룩 있으면 그거 해결해야할듯
                if status[j][num] == -1:
                    continue
                elif status[j][num] == status[j][num-1]:
                    change = True
                    status[j][num-1]

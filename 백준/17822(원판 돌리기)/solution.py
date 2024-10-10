from collections import deque
import copy

N, M, T = map(int, input().split())
status = [deque() for _ in range(N+1)]

for i in range(1, N+1):
    temp = list(map(int, input().split()))
    for j in temp:
        status[i].append(j)

for i in range(T):
    x, d, k = map(int, input().split())
    # 돌려돌려 돌림판
    for j in range(1, N+1):
        # j가 x의 배수라면 움직여야하는 원판
        if j % x ==0:
            # k만큼 움직이기
            if d == 0:
                for move in range(k):
                    temp = status[j].pop()
                    status[j].appendleft(temp)
            elif d == 1:
                for move in range(k):
                    temp = status[j].popleft()
                    status[j].append(temp)

    after = copy.deepcopy(status)
    flag = True
    # 전체 순회 및 체크
    for j in range(1, N+1):
        if sum(status[j]) == -M:
            continue
        else:
            for num in range(M):
                if status[j][num] == -1:
                    continue
                if j < N:
                    if num == M-1:
                        if status[j][num] == status[j][num-1]:
                            after[j][num] = -1
                            after[j][num-1] = -1
                            flag = False
                        if status[j][num] == status[j+1][num]:
                            after[j][num] = -1
                            after[j+1][num] = -1
                            flag = False
                        if status[j][num] == status[j][0]:
                            after[j][num] = -1
                            after[j][0] = -1
                            flag = False
                    else:
                    # 마지막일떄
                        if status[j][num] == status[j][num-1]:
                            after[j][num] = -1
                            after[j][num-1] = -1
                            flag = False
                        if status[j][num] == status[j][num+1]:
                            after[j][num] = -1
                            after[j][num+1] = -1
                            flag = False
                        if status[j][num] == status[j+1][num]:
                            after[j][num] = -1
                            after[j+1][num] = -1
                            flag = False
                else:
                    if num == M-1:
                        if status[j][num] == status[j][num-1]:
                            after[j][num] = -1
                            after[j][num-1] = -1
                            flag = False
                        if status[j][num] == status[j][0]:
                            after[j][num] = -1
                            after[j][0] = -1
                            flag = False
                    else:
                    # 마지막일떄
                        if status[j][num] == status[j][num-1]:
                            after[j][num] = -1
                            after[j][num-1] = -1
                            flag = False
                        if status[j][num] == status[j][num+1]:
                            after[j][num] = -1
                            after[j][num+1] = -1
                            flag = False         
    if flag:
        sumValue = 0
        count = 0
        for j in range(1, N+1):
            for num in range(M):
                if after[j][num] != -1:
                    sumValue+= after[j][num]
                    count+=1
        for j in range(1, N+1):
            for num in range(M):
                if after[j][num] != -1:
                    if after[j][num] > (sumValue/count):
                        after[j][num]-=1
                    elif after[j][num] < (sumValue/count):
                        after[j][num]+=1
    status = after

sumValue = 0
for j in range(1, N+1):
    for num in range(M):
        if after[j][num] != -1:
            sumValue+= after[j][num]
print(sumValue)

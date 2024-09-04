from collections import deque

def solution():
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    start =1
    temp = [0]
    for i in arr:
        #가능한 모든 경우의 수 탐색
        # 시간복잡도 에바일거같긴함
        num_len = len(temp)
        for j in range(num_len):
            if (temp[j]+i) not in temp:
                temp.append(temp[j]+i)
    while True:   
        if not (start in temp):
            break
        start += 1
    print(start)

        
    return 0


solution()


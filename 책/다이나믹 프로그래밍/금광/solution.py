from collections import deque


def solution():
    play = int(input())
    dy = [-1, 0, 1]
    for i in range(play):
        # n은 행 개수, m은 열 개수
        n, m = map(int, input().split())
        arr = []
        value = list(map(int, input().split()))
        value = deque(value)
        for j in range(n):
            temp_arr = []
            for k in range(m):
                temp_arr.append(value.popleft())
            arr.append(temp_arr)
        # 한열씩
        for i in range(1, m):
            # 한 행씪
            for j in range(n):
                # 이전값들 방향 확인
                maxValue = 0
                for dir in dy:
                    beforeRow = j + dir
                    if beforeRow >= 0 and beforeRow < n and maxValue < arr[beforeRow][i-1]:
                        maxValue = arr[beforeRow][i-1]
                arr[j][i] += maxValue
        print(max(map(max, arr)))
    return 0


solution()

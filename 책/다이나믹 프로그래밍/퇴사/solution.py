
def solution():
    n = int(input())
    arr = []
    for i in range(n):
        cost, money = map(int,input().split())
        arr.append([cost,money,0])
    for i in range(n):
        #현재 시간 + 걸리는 시간이 날짜보다 길면 안됨
        if i + arr[i][0] < n:
            if arr[i+arr[i][0]][2] < arr[i][1] + arr[i][2]:
                arr[i+arr[i][0]][2] = arr[i][1] + arr[i][2]
    max = 0
    for i in range(n):
        if max < arr[i][2]:
            max = arr[i][2]
    print(max)
    return 0


solution()

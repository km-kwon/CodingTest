
def solution():
    n = int(input())
    arr = []
    for i in range(n):
        temp = list(map(int,input().split()))
        arr.append(temp)
    for i in range(1,n):
        for j in range(len(arr[i])):
            if j == 0:
                arr[i][j] = arr[i][j]+ arr[i-1][j]
            elif j == (len(arr[i])-1):
                arr[i][j] = arr[i][j] +arr[i-1][j-1]
            else:
                arr[i][j] = arr[i][j] + max(arr[i-1][j], arr[i-1][j-1])
    print(max(arr[n-1]))
    return 0


solution() 

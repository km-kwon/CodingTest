t=int(input())
for i in range(t):
    n =int(input())
    arr = [0] *(n + 1)
    arr[1] = 1
    arr[2] = 2
    arr[3] = 3
    for j in range(4,n+1):
        arr[j] = arr[j-1] - arr[j-2] + arr[j-3]
    print(arr[n])
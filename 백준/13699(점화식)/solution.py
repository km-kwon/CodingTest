n = int(input())

arr = [0] * (n+1)
arr[0] = 1
for i in range(1,n+1):
    for j in range(i):
        arr[i] += arr[i-j-1] * arr[j]
print(arr[n])
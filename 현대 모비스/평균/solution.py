N = int(input())
arr = list(map(int, input().split()))
maxValue = max(arr)
for i in range(N):
    arr[i] = arr[i] / maxValue * 100

print(sum(arr) / N)


n = int(input())
arr = []
arr = list(map(int,input().split()))

arr.sort()

total = [0] * n
total[0] = arr[0]
for i in range(1,n):
    total[i] = total[i-1] + arr[i]

print(sum(total))
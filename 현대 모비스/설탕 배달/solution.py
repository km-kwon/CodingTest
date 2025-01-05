N = int(input())

# DP로 해결하면 될듯 함
arr = [0] * (N + 1)
for i in range(N + 1):
    if i == 6:
        break
    if i == 3 or i == 5:
        arr[i] = 1
    else:
        arr[i] = -1


for i in range(6, N + 1):
    if arr[i - 3] != -1 and arr[i - 5] != -1:
        arr[i] = min(arr[i - 3] + 1, arr[i - 5] + 1)
        continue
    if arr[i - 3] != -1:
        arr[i] = arr[i - 3] + 1
        continue
    elif arr[i - 5] != -1:
        arr[i] = arr[i - 5] + 1
        continue
    arr[i] = -1


print(arr[N])

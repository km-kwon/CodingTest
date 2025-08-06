n,k = map(int,input().split())
arr = list(map(int,input().split()))

left, right = 1, arr[-1]

result = 0
while left<=right:
    mid = (left+right) // 2 
    cur = 0
    count = 0
    for i in arr:
        if cur <= i:
            count += 1
            cur = i + mid
        if count > k:
            break
    if count > k:
        left = mid+1
    else:
        result = mid
        right = mid-1
print(result)

n,d,k,c = map(int,input().split())

maxValue = 0

arr = []
check  = {}
for i in range(n):
    arr.append(int(input()))

for i in range(k):
    arr.append(arr[i])
    if not arr[i] in check:
        check[arr[i]] = 1
    else:
        check[arr[i]] +=1
start  = 0
end = k
while end < len(arr):
    if not c in check:
        maxValue = max(maxValue, len(check)+1)
    else:
        maxValue = max(maxValue, len(check))

    if not arr[end] in check:
        check[arr[end]] = 1
    else:
        check[arr[end]] +=1

    if check[arr[start]] == 1:
        del check[arr[start]]
    else:
        check[arr[start]] -= 1
    start +=1
    end +=1
print(maxValue)
N,S = map(int,input().split())

arr = list(map(int,input().split()))
value = 0
start = 0
length = 1e9
for i in range(0, N):
    value += arr[i]
    while start<=i and value >=S:
        length = min(length, i-start+1)
        value-=arr[start]
        start+=1
if length == 1e9:
    print(0)
else:
    print(length)
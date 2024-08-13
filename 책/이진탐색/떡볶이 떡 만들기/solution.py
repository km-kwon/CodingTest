def solution():
    n, length = map(int, input().split())
    arr = list(map(int,input().split(' ')))
    end = max(arr)
    start = 1
    avg = int((end+start)/2)
    while True:
        sum = 0
        avg = int((end+start)/2)
        for i in arr:
            if i>avg:
                sum += (i-avg)
        if sum > length:
            start = avg+1
        elif sum<length:
            end = avg-1
        elif sum == length:
            break
        if end < start:
            break
    print(avg)
      

    return 0


solution()

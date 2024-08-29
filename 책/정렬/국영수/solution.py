def solution():
    n = int(input())
    arr = []
    for i in range(n):
        curName, kor, eng,math = input().split()
        arr.append((int(kor), int(eng), int(math),curName))
    arr = sorted(arr,key = lambda x:(-x[0],x[1],-x[2],x[3]))
    for i in arr:
        print(i[3])
    return 0
solution()

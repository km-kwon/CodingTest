import copy
n, m = map(int, input().split())

arr = []


def cal(arr, n, m):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(1, n+1):
        temp = copy.deepcopy(arr)
        if not i in temp:
            temp.append(i)
            cal(temp, n, m)


cal(arr, n, m)

import copy
def cal(row, col, arr):
    temp = copy.deepcopy(arr)
    maxLen = 0
    result =[]
    for i in range(row):
        row_result = []
        dic = {}
        sort_temp  = []
        for j in range(col):
            if temp[i][j] == 0:
                continue
            if not temp[i][j] in dic:
                dic[temp[i][j]] = [1,temp[i][j]]
            else: 
                dic[temp[i][j]][0] +=1
        for j in dic.values():
            sort_temp.append(j)
        sort_temp = sorted(sort_temp,key=  lambda x:(x[0],x[1]))
        for j in sort_temp:
            row_result.append(j[1])
            row_result.append(j[0])
        maxLen = max(maxLen, len(row_result))
        result.append(row_result)
    for i in range(len(result)):
        for j in range(maxLen-len(result[i])):
            result[i].append(0)
    return result


def solution():
    r, c, k = map(int,input().split())
    r = r-1
    c = c-1
    time = 0
    arr = []
    for i in range(3):
        arr.append(list(map(int,input().split())))
    while True:
        if arr[r][c] == k:
            print(time)
            break
        arr = cal(len(arr), len(arr[0]), arr)
        time+=1
        if time > 100:
            print(-1)
            break
        if arr[r][c] == k:
            print(time)
            break
        arr = list(zip(*arr))
        arr = cal(len(arr), len(arr[0]), arr)
        arr = list(zip(*arr))
        time+=1
        if time > 100:
            print(-1)
            break
        if arr[r][c]==k:
            print(time)
            break
    return

solution()




""" import copy

maxLen = 0

def Roperation(arr):
    global maxLen
    maxLen = 0
    lenRow = len(arr)
    lenCol = len(arr[0])
    for i in range(lenRow):
        countArr = {}
        for j in range(lenCol):
            if arr[i][j] == 0:
                break
            if not arr[i][j] in countArr: 
                countArr[arr[i][j]] = [1, arr[i][j]]
            else:
                countArr[arr[i][j]][0] +=1
        tempArr = []
        for k in countArr.values():
            tempArr.append(k)
        tempArr = sorted(tempArr ,key = lambda x: (x[0],x[1]))
        tempArr2 = []
        for k in tempArr:
            tempArr2.append(k[1])
            tempArr2.append(k[0])
        arr[i] = tempArr2
        maxLen = max(maxLen, len(arr[i]))
    for i in range(lenRow):
        for j in range(maxLen-(len(arr[i]))):
            arr[i].append(0)
    if maxLen>100:
        for i in range(arr):
            finalArr = []
            for j in range(100):
                finalArr.append(arr[i][j])
            arr[i] = finalArr
    return


def Coperation(arr):
    global maxLen
    maxLen = 0
    lenRow = len(arr)
    lenCol = len(arr[0])
    returnArr= []
    for j in range(lenCol):
        countArr = {}
        for i in range(lenRow):
            if arr[i][j] == 0:
                continue
            if not arr[i][j] in countArr: 
                countArr[arr[i][j]] = [1, arr[i][j]]
            else:
                countArr[arr[i][j]][0] +=1
        tempArr = []
        for k in countArr.values():
            tempArr.append(k)
        tempArr = sorted(tempArr ,key = lambda x: (x[0],x[1]))
        tempArr2 = []
        for k in tempArr:
            tempArr2.append(k[1])
            tempArr2.append(k[0])
        maxLen = max(maxLen, len(tempArr2))
        returnArr.append(tempArr2)
    for i in range(maxLen - lenRow):
        arr.append([0]*lenCol)
    for i in range(len(returnArr)):
        for j in range(len(returnArr[i])):
            arr[j][i] = returnArr[i][j]
    if maxLen > 100:
        for i in range(100):
            finalArr = []
            for j in range(arr[0]):
                finalArr.append(arr[i][j])
            arr[i] = finalArr
    return 
def solution():
    r,c,k = map(int,input().split())
    r = r-1
    c = c-1
    arr = []
    for i in range(3):
        arr.append(list(map(int,input().split())))
    count = 0
    while True:
        if  arr[r][c] == k:
            break
        Roperation(arr)
        count+=1
        if  arr[r][c] == k:
            break
        Coperation(arr)
        count+=1
    print(count)
    return
 

solution() """
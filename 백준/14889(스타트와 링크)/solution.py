n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

team = [-1]*n

minValue = 0

def sol(start,n,team):
    global arr
    if not -1 in team:
        aval1 = 0
        aval2 = 0
        start = []
        link = []
        for i in range(n):
            if team[i] == 1:
                start.append(i)
                for j in start:
                    aval1 += (arr[j-1][i-1] + arr[i-1][j-1])
            elif team[i] ==2:
                link.append(i)
                for j in start:
                    aval2 += (arr[j-1][i-1] + arr[i-1][j-1])
        
    for i in range(start,n):
        team[i] = 1
        sol(i+1,n,team)
        team[i] = 2
        sol(i+1,n,team)
    return

sol(0,n,team)
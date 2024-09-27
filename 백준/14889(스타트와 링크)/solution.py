n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

team = [-1]*n

minValue = 1e9


def sol(start, n, team, num1):
    global arr
    global minValue
    if num1 == n/2 :
        start = 0
        link = 0
        for i in range(n):
            for j in range(i,n):
                if team[i] == team[j] and team[i] == 1 and i!=j:
                    start+= (arr[j][i] + arr[i][j])
                elif team[i] == team[j] and team[i] == -1 and i!=j:
                    link += (arr[j][i] + arr[i][j])
        minValue = min(minValue, abs(start-link))
        return
    else:
        for i in range(start, n):
            team[i] = 1
            sol(i+1, n, team, num1+1)
            team[i] = -1
    return


sol(0, n, team,0)

print(minValue)

### 네트워크 연결결

성공 코드

```
n = int(input())
m = int(input())

par = [0] * n
for i in range(n):
    par[i] = i

cost = []
for i in range(m):
    n1, n2, c = map(int, input().split())
    cost.append((c, (n1 - 1, n2 - 1)))
cost.sort()


def find_par(par, node):
    if par[node] == node:
        return node
    else:
        return find_par(par, par[node])


minValue = 0

for c, (n1, n2) in cost:
    par_n1 = find_par(par, n1)
    par_n2 = find_par(par, n2)
    if par_n1 != par_n2:
        if par_n1 > par_n2:
            par[par_n1] = par_n2
        elif par_n1 < par_n2:
            par[par_n2] = par_n1
        minValue += c

print(minValue)

```

# 사용 개념

-   크루스칼 알고리즘즘

---

# 새겨놔야 할점

-  이건 너무 기본적이네.

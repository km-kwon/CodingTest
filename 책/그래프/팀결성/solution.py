from collections import deque


def solution():

    n, m = map(int, input().split())
    student = [-1]*(n+1)
    for i in range(n+1):
        student[i] = i

    def checkSamTeam(a, b):
        if student[a] == student[b]:
            print("YES")
        else:
            print("NO")
        return

    def findParent(num):
        if student[num] == num:
            return student[num]
        else:
            return findParent(student[num])

    def makeSameTeam(a, b):
        parent_a = findParent(a)
        parent_b = findParent(b)

        if parent_a < parent_b:
            student[b] = parent_a
        else:
            student[a] = parent_b
        return

    for i in range(m):
        act, a, b = map(int, input().split())
        if act == 0:
            makeSameTeam(a, b)
        elif act == 1:
            checkSamTeam(a, b)
    return 0


solution()

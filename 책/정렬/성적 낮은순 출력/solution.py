def solution():
    n = int(input())
    arr = []
    for i in range(n):
        name, grade = input().split(' ')
        arr.append([name, int(grade)])
    arr = sorted(arr, key=lambda student: student[1])

    for i in arr:
        print(i[0])
    return 0


solution()

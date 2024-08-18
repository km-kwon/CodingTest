from collections import deque


def solution():
    n, price = map(int,input().split(' '))
    arr= [-1]*(price+1)
    numbers = []
    numbers.sort()
    for i in range(n):
        numbers.append(int(input()))
    for i in numbers:
        for j in range(1,price+1):
            if j % i==0 and arr[j] == -1:
                arr[j] = j//i
            elif j % i ==0 and arr[j] > j//i:
                arr[j] = j//i
            elif arr[j] == -1 and j-i > 0 and arr[j-i] != -1:
                arr[j] = arr[j-i] + 1
            elif j-i >0 and arr[j-i] != -1 and arr[j] > arr[j-i] +1:
                arr[j] = arr[j-i] + 1
    print(arr[price])
solution()

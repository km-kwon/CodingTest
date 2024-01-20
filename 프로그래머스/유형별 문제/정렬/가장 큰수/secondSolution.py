def solution(numbers):
    answer = ''
    list = []
    for i in numbers:
        list.append(str(i))
    list.sort(key=lambda x: x*3, reverse=True)
    return str(int("".join(list)))


solution([6, 10, 2])
solution([3, 30, 34, 5, 9])

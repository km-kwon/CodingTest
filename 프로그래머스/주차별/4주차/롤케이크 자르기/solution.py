import collections


def solution(topping):
    answer = 0
    topping = collections.deque(topping)
    dic1 = collections.Counter(topping)
    dic2 = {}
    while len(dic1) >= len(dic2):
        cur = topping.popleft()
        dic1[cur] -= 1
        if dic1[cur] == 0:
            del dic1[cur]
        if not cur in dic2:
            dic2[cur] = 1
        else:
            dic2[cur] += 1
        if len(dic1) == len(dic2):
            answer += 1

    return answer


solution([1, 2, 1, 3, 1, 4, 1, 2])
solution([1, 2, 3, 1, 4])

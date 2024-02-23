from collections import deque


def solution(order):
    answer = 0
    i = 1
    stack = deque()
    cur = 0
    while i != (len(order)+1):
        stack.append(i)
        while stack and stack[-1] == order[cur]:
            answer += 1
            cur += 1
            stack.pop()
        i += 1
    return answer

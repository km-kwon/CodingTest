from collections import deque


def solution(prices):
    answer = [0] * (len(prices))
    que = deque()
    que.append([prices[0], 0])
    for i in range(1, len(prices)):
        while que and que[len(que)-1][0] > prices[i]:
            cur = que.pop()
            answer[cur[1]] = i - cur[1]
        que.append([prices[i], i])
    for i in que:
        answer[i[1]] = len(prices)-1-i[1]
    return answer

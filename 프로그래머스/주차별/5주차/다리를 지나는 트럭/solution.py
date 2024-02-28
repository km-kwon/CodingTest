from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 2
    truck_weights = deque(truck_weights)
    bridge_que = deque()
    bridge_que.append([truck_weights.popleft(), 1])
    bridge_weight = bridge_que[0][0]
    while bridge_que:
        if not bridge_que:
            bridge_weight += truck_weights[0]
            bridge_que.append([truck_weights.popleft(), answer])
        else:
            if (answer - bridge_que[0][1]) == bridge_length:
                bridge_weight -= bridge_que[0][0]
                bridge_que.popleft()
                if not bridge_que and not truck_weights:
                    break
            if truck_weights and (bridge_weight + truck_weights[0]) <= weight:
                bridge_weight += truck_weights[0]
                bridge_que.append([truck_weights.popleft(), answer])
        answer += 1
    return answer


# solution(2, 10,	[7, 4, 5, 6])
# solution(10, 10,	[10])
solution(10, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])

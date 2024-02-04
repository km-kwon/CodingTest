import heapq


def solution(operations):
    arr = []
    for i in operations:
        operation = i[0]
        num_value = int(i[2:])
        if operation == "I":
            heapq.heappush(arr, num_value)
            continue
        if operation == "D" and num_value == 1:
            if len(arr) != 0:
                max_value = max(arr)
                arr.remove(max_value)
                continue
        if operation == "D" and num_value == -1:
            if len(arr) != 0:
                heapq.heappop(arr)
    if len(arr) == 0:
        answer = [0, 0]
    else:
        answer = [max(arr), heapq.heappop(arr)]
    return answer


# solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
solution(["I -45", "I 653", "D 1", "I -642",
         "I 45", "I 97", "D 1", "D -1", "I 333"])

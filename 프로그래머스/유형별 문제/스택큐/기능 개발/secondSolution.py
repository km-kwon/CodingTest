def solution(progresses, speeds):
    answer = []
    day = 0
    while progresses:
        count = 0
        day += 1
        for i in range(len(progresses)):
            if speeds[i] * day + progresses[i] < 100:
                break
            count += 1
        for i in range(count):
            progresses.pop(0)
            speeds.pop(0)
        if count != 0:
            answer.append(count)

    return answer


# solution([93, 30, 55],	[1, 30, 5])
solution([95, 90, 99, 99, 80, 99],	[1, 1, 1, 1, 1, 1])

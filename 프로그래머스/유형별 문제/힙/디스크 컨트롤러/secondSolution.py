import heapq


def solution(jobs):
    answer = []
    ing = -1
    queue = []
    time = 0
    jobs.sort()
    cur_job = []
    for i in jobs:
        heapq.heappush(queue, [i[1], i[0]])
    while True:
        if ing == -1 and queue and time >= queue[0][1]:
            ing = 0
            cur_job.append(heapq.heappop(queue))
        time += 1
        if ing != -1:
            ing += 1
        if cur_job:
            if ing == cur_job[0][0]:
                answer.append(time - cur_job[0][1])
                cur_job.pop(0)
                ing = -1
        if not cur_job and not queue:
            break
    print(int(sum(answer)/len(answer)))
    return int(sum(answer)/len(answer))


solution([[0, 10], [2, 10], [9, 10], [15, 2]])
solution([[0, 3], [1, 9], [2, 6]])

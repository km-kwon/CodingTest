import heapq


def solution(book_time):
    answer = 0
    time = []
    heap = []
    for i in book_time:
        i[0] = int(i[0][:2]) * 60 + int(i[0][3:])
        i[1] = int(i[1][:2]) * 60 + int(i[1][3:]) + 10
        time.append(i)
    time.sort()
    for i in time:
        if not heap:
            heapq.heappush(heap, i[1])
        else:
            while heap and heap[0] <= i[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, i[1])
        if answer < len(heap):
            answer = len(heap)
    return answer

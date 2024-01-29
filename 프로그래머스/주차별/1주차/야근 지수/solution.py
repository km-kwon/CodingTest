import heapq


def solution(n, works):
    if sum(works) <= n:
        return 0
    heap = []
    for i in works:
        heap.append(-i)
    heapq.heapify(heap)

    for i in range(n):
        heapq.heappush(heap, -(-(heapq.heappop(heap)) - 1))

    sum1 = 0
    for i in heap:
        sum1 += i*i
    return sum1


solution(4, [4, 3, 3])
solution(1, [2, 1, 2])
solution(3, [1, 1])

import heapq

def solution():
    n = int(input())
    m = int(input())
    arr = [[0]*n for _ in range(n)]
    for i in range(m):
        start, end, cost = map(int,input().split())
        if arr[start-1][end-1] == 0:
            arr[start-1][end-1] = cost
            continue
        arr[start-1][end-1] = min(arr[start-1][end-1], cost)
    
    def find_route(start):
        cost = [1e9] * n
        cost[start] = 0
        heap = []
        heapq.heappush(heap,(0,start))
        while heap:
            cur_cost, cur_start= heapq.heappop(heap)
            for i in range(len(arr[cur_start])):
                if arr[cur_start][i] != 0 and cost[i] > cost[cur_start]+arr[cur_start][i]:
                    cost[i] = cost[cur_start]+arr[cur_start][i]
                    heapq.heappush(heap,(cost[i],i))
        for i in cost:
            print(i, end = " ")
        print()

    for i in range(n):
        find_route(i)
    return 0
solution()

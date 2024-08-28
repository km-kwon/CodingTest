import heapq




def solution():

    def find_parent(check,node):
        if check[node] == node:
            return node
        return find_parent(check,check[node])
    
    def edit_parent(check,node1,node2):
        parent_node1 = find_parent(check,node1)
        parent_node2 = find_parent(check,node2)
        if parent_node1 > parent_node2:
            check[parent_node1] = parent_node2
        elif parent_node1 < parent_node2:
            check[parent_node2] = parent_node1
        return

    n, m = map(int,input().split())
    arr = []
    check =[-1] * n 
    for i in range(n):
        check[i] = i
    cost = 0 
    for i in range(m):
        src, dst, enter_cost = map(int,input().split())
        heapq.heappush(arr, (enter_cost,src,dst))

        
    while arr:
        cur_cost,src,dst = heapq.heappop(arr)
        if find_parent(check,src) != find_parent(check,dst):
            edit_parent(check,src,dst)
        else:
            cost += cur_cost
    print(cost)
    return 0


solution()

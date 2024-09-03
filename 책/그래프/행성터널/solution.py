import heapq
def solution():
    n  = int(input())
    arr = []
    edge = []
    parent = []
    total_cost = 0
    for i in range(n):
        parent.append(i)
    for i in range(n):
        x,y,z = map(int,input().split())
        arr.append((x,y,z))
    for i in range(n):
        for j in range(i+1,n):
            x = abs(arr[i][0]-arr[j][0])
            y = abs(arr[i][1]-arr[j][1])
            z = abs(arr[i][2]-arr[j][2])
            heapq.heappush(edge, (min(x,y,z),i,j))

    def find_parent(node):
        if parent[node] == node:
            return node
        return find_parent(parent[node])

    while edge:
        cost, node1, node2 = heapq.heappop(edge)
        parent_node1 = find_parent(node1)
        parent_node2 = find_parent(node2)
        if parent_node1 != parent_node2:
            if parent_node1 > parent_node2:
                parent[parent_node1] = parent_node2
            else:
                parent[parent_node2] = parent_node1
            total_cost += cost
    print(total_cost)
    return 0


solution()

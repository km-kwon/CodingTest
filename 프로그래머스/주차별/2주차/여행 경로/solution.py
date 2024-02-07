def solution(tickets):
    answer = ["ICN"]
    dic = {}
    queue = ["ICN"]
    for i in tickets:
        if not i[0] in dic:
            dic[i[0]] = [i[1]]
            continue
        dic[i[0]].append(i[1])
    for i in dic.values():
        i.sort()
    while queue:
        cur = queue.pop(0)
        if dic[cur]:
            for i in range(len(dic[cur])):
                if dic[cur][i] in dic:
                    queue.append(dic[cur][i])
                    answer.append(dic[cur][i])
                    dic[cur].pop(i)
                    break
    if dic[cur]:
        answer.append(dic[cur][0])
    return answer


# solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])

# solution([["ICN", "SFO"], ["ICN", "ATL"],
#          ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])

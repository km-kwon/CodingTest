def solution(gems):
    answer = [0, len(gems)-1]
    type = len(set(gems))
    dic = {gems[0]: 1}
    left, right = 0, 0
    while left < len(gems) and right < len(gems) and left <= right:
        if len(dic) == type:
            if (answer[1] - answer[0]) > (right-left):
                answer[0], answer[1] = left, right
            dic[gems[left]] -= 1
            if dic[gems[left]] == 0:
                del dic[gems[left]]
            left += 1
            continue
        if len(dic) < type:
            right += 1
            if right >= len(gems):
                break
            if not gems[right] in dic:
                dic[gems[right]] = 1
            else:
                dic[gems[right]] += 1
    answer[0], answer[1] = answer[0] + 1, answer[1]+1
    return answer


solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
solution(["AA", "AB", "AC", "AA", "AC"])
solution(["XYZ", "XYZ", "XYZ"])
solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])

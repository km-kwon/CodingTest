from collections import deque


def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        skill_check = deque(skill)
        flag = True
        for j in i:
            if j in skill_check and skill_check[0] == j:
                skill_check.popleft()
                continue
            if j in skill_check and skill_check[0] != j:
                flag = False
                break
        if flag:
            answer += 1
    return answer


solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])

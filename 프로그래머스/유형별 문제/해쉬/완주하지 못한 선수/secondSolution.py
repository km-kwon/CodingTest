
def solution(participant, completion):
    answer = ''
    value_dic = {}
    for name in participant:
        if (value_dic.get(name, -1)) != -1:
            value_dic[name] += 1
            continue
        value_dic[name] = 1
    for name in completion:
        value_dic[name] -= 1
        if value_dic[name] == 0:
            value_dic.pop(name)
    return list(value_dic)[0]


"""
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]

sort 후 비교  시간 복잡도 O(N)
및 zip 사용
"""
"""
import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

collection 사용 => collection에서의 객체끽리는 뺴기가 가능 및 자동 삭제
"""


# solution(["leo", "kiki", "eden"], ["eden", "kiki"])
solution(["marina", "josipa", "nikola", "vinko", "filipa"],
         ["josipa", "filipa", "marina", "nikola"])
solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])

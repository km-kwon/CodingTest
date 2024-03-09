import collections

def solution(k, tangerine):
    answer = 0
    dic = collections.Counter(tangerine)
    dic = dict(sorted(dic.items(), key = lambda x:x[1], reverse = True))
    for i in dic.values():
        k -= i
        answer +=1
        if k <= 0:
            break
    return answer
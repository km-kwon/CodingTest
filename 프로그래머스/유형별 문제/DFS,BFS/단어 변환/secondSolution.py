def solution(begin, target, words):
    answer = 0
    dic = dict.fromkeys(words, -1)
    dic[begin] = 0
    queue = [begin]
    if not (target in words):
        return 0
    while queue:
        cur_word = queue.pop(0)
        for key in dic:
            if dic[key] == -1:
                count = 0
                for i in range(len(cur_word)):
                    if cur_word[i] != key[i]:
                        count += 1
                if count == 1:
                    dic[key] = dic[cur_word] + 1
                    queue.append(key)
    return dic[target]


solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log", "cog"])
solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log"])

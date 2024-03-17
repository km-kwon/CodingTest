def solution(s):
    answer = 0
    for i in range(len(s)+1):
        for j in range(i, (len(s)+1)):
            sub = s[i:j]
            pali = sub[::-1]
            if sub == pali and answer <len(pali):
                answer  = len(pali)
    return answer
def solution(number, k):
    answer = []
    for i in number:
        if not answer:
            answer.append(i)
            continue
        while answer and answer[-1] < i and k > 0:
            answer.pop()
            k -= 1
        answer.append(i)
    if k > 0:
        answer = answer[:-k]
    return ''.join(answer)


# solution("1924", 2)
solution("1231234", 3)
solution("4177252841", 4)

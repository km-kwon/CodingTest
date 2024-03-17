def solution(brown, yellow):
    answer = []
    for i in range(1, yellow+1):
        if yellow % i == 0:
            yellow_x = i
            yellow_y = int(yellow/i)
            if ((yellow_x * 2) + 4 + (yellow_y * 2)) == brown:
                answer.append(yellow_x + 2)
                answer.append(yellow_y + 2)
                answer.sort(reverse=True)
                break
    return answer

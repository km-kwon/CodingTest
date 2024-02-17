def solution(sequence):
    sequence2 = sequence[:]
    purse = 1
    for i in range(len(sequence)):
        sequence[i] *= purse
        purse *= -1
        sequence2[i] *= purse
    max_sum = 0
    tmp = 0
    for s in sequence:
        tmp += s
        if tmp < 0:
            tmp = 0
        max_sum = max(max_sum, tmp)
    tmp = 0
    for s in sequence2:
        tmp += s
        if tmp < 0:
            tmp = 0
        max_sum = max(max_sum, tmp)
    return max_sum


solution([2, 3, -6, 1, 3, -1, 2, 4])

solution([2, 3, -6, -1, 3, -1, 2, 4])

solution([2, 3, -6, 1, -3, -1, -2, 15])

'''
def solution(sequence):
    answer = 0
    left, right = 0, 1
    max = 0
    start = 0
    if sequence[0] > 0:
        start = 1
    else:
        start = -1
    while right <= len(sequence)-1:
        if sequence[right]*start < 0:
            start = start * -1
            max += abs(sequence[right])
            if right == len(sequence)-1:
                if max > answer:
                    answer = max
            right += 1
            continue
        if left != right-1:
            if max > answer:
                answer = max
        left = right
        max = abs(sequence[left])
        right += 1
    return answer

'''

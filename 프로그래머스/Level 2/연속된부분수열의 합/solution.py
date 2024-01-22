def solution(sequence, k):
    position = []
    position_value = []
    start = 0
    end = 0
    sum = sequence[0]
    while start <= end and end < len(sequence):
        if sum < k:
            if end+1 == len(sequence):
                break
            end += 1
            sum += sequence[end]
            continue
        if sum > k:
            sum -= sequence[start]
            start += 1
            continue
        if sum == k:
            position_value.append(end-start)
            position.append([start, end])
            if end+1 == len(sequence):
                break
            end += 1
            sum += sequence[end]
    # print(position[position_value.index(min(position_value))])
    return position[position_value.index(min(position_value))]


# solution([1, 2, 3, 4, 5], 7)
solution([1, 1, 1, 2, 3, 4, 5], 5)
solution([2, 2, 2, 2, 2], 6)


'''
def solution(sequence, k):
    position = []
    position_idx = []
    for i in range(len(sequence)):
        value = 0
        if sequence[i] > k:
            break
        for j in range(i, len(sequence)):
            value += sequence[j]
            if value > k:
                break
            if value == k:
                position.append([i, j])
                position_idx.append(j-i)
                break
    print(position[position_idx.index(min(position_idx))])
    return position[position_idx.index(min(position_idx))]

'''

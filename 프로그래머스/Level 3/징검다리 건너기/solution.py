def solution(stones, k):
    answer = 0
    left, right = 0, max(stones)
    while left <= right:
        mid = (left+right)//2
        count = 0
        for i in range(0, len(stones)):
            if stones[i] - mid <= 0:
                count += 1
                if count == k:
                    break
                continue
            count = 0
        if count < k:
            left = mid+1
            continue
        answer = mid
        right = mid-1
    return answer


solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)


'''
def solution(stones, k):
    answer = 0
    while True:
        min_value = max(stones)
        for i in stones:
            if min_value > i and i != 0:
                min_value = i
        count = 0
        for i in range(1, len(stones)):
            if stones[i] <= 0 and stones[i-1] <= 0:
                count += 1
                if count == k-1:
                    return answer
                continue
            count = 0
        for i in range(len(stones)):
            if stones[i] == 0:
                continue
            stones[i] -= min_value
        answer += min_value
'''

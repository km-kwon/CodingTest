def solution(people, limit):
    answer = 0
    people.sort()
    left, right = 0, len(people)-1
    while left <= right:
        if people[right] + people[left] <= limit and len(people) != 1:
            left += 1
            right -= 1
            answer += 1
            continue
        right -= 1
        answer += 1
    return answer


solution([70, 50, 80, 50], 100)
solution([70, 80, 50], 100)

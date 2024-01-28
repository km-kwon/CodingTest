def solution(n, times):
    answer = 0
    left = min(times)
    right = max(times) * n
    while left <= right:
        mid = (left+right)//2
        passed = 0
        for time in times:
            passed += mid // time

            if passed >= n:
                break

        if passed >= n:
            answer = mid
            right = mid - 1
            continue
        if passed < n:
            left = mid + 1

    return answer


solution(6,	[7, 10])

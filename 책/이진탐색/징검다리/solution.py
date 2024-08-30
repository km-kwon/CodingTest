
def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    start ,end =0,distance
    while start<=end:
        cur = 0
        mid = (start+end)// 2
        count = 0
        for i in rocks:
            if i-cur < mid:
                count+=1
            else:
                cur = i
        if count > n:
            end = mid-1
        else:
            start = mid+1
    return answer

solution(25,	[2, 14, 11, 21, 17],	2)

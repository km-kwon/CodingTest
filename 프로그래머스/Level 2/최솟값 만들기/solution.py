def solution(A,B):
    a = sorted(A)
    b = sorted(B, reverse=True)
    count = 0
    for i,j in zip(a,b):
        count += i*j
    """ for i in range(len(a)):
        count += (a[i] * b[i]) """
    return count


solution([1, 4, 2],[5, 4, 4])
solution([1,2]	,[3,4])

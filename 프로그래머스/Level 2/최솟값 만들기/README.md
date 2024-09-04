### 최솟값 만들기

---

성공 코드

```
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

```

회고

-   그리디 문제
-   순간순간 최선의 선택

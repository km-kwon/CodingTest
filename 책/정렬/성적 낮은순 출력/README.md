### 성적 낮은 순서로 학생 출력학기

성공 코드

```
def solution():
    n = int(input())
    arr = []
    for i in range(n):
        name, grade = input().split(' ')
        arr.append([name, int(grade)])
    arr = sorted(arr, key=lambda student: student[1])

    for i in arr:
        print(i[0])
    return 0


solution()

```

사용 개념

- sort 활용법
- lambda 활용

---

# 새겨놔야 할점

- sort는 람다의 활용법이 중요하다.

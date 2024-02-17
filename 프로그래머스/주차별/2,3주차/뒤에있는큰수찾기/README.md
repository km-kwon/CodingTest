### 뒤에있는큰수찾기

---

성공 코드

```
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = [0]
    for i in range(1, len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
            continue
        stack.append(i)
    return answer
```

회고

- 문제를 정확히 읽지 않아 삽질을 오랫동안 함
- 이중 for 문 시간 복잡도 문제 해결을 위해 삽질
- stack을 활용했지만 이것도 결국 시간복잡도가 똑같지 않나 고민

```
for : O(n)
while : O(1) == 스택의 길이만큼 돌수 있지만, 한 데이터당 한번만 pop할수 있으므로

O(n) * O(1) = O(n)입니다.
라고 하는데 스택의 길이가 n-1이면 n**2아닌가...

뭔가 "가장 가까이"라는 말이 있으면 스택으로 접근하는 것이 효율적일듯
```

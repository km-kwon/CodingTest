### 올바른 괄호

---

성공 코드

```
def solution(s):
    stack = []
    for i in s:
        if not stack and i == ")":
            return False
        if i == ")":
            stack.pop()
            continue
        if i == "(":
            stack.append(i)
    if stack:
        return False
    return True

```

사용 개념

- stack 사용


---

다른 사람 코드 중 인상 깊었던 것

```
def is_pair(s):
    st = list()
    for c in s:
        if c == '(':
            st.append(c)

        if c == ')':
            try:
                st.pop()
            except IndexError:
                return False

    return len(st) == 0
```

사용 개념

- try 로 시행
- IndexError로 예외 처리

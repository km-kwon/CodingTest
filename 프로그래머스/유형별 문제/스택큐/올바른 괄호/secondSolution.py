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


solution("()()")
solution("(())()")
solution(")()(")
solution("(()(")

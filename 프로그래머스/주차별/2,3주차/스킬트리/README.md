### 스킬트리

---

성공 코드

```
from collections import deque
def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        skill_check = deque(skill)
        flag = True
        for j in i:
            if j in skill_check and skill_check[0] == j:
                skill_check.popleft()
                continue
            if j in skill_check and skill_check[0] != j:
                flag = False
                break
        if flag:
            answer += 1
    return answer
```

회고

- 시간 복잡도에 너무 얽매어서 해결 오래걸림
- 선행 사건을 위해서는 디큐 사용

인상깊은 코드

```
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer
```

- 파이썬은 for-else 사용 가능
- for 문에서 break 되지 않으면 else 실행

### 표 편집

---

성공 코드

```
def solution(n, k, cmd):
    cur = k
    table = { i:[i - 1, i + 1] for i in range(n) }
    answer = ['O'] * n
    table[0] = [None, 1]
    table[n - 1] = [n - 2, None]
    stack = []
    for c in cmd:
        if c == "C":
            # 삭제
            answer[cur] = 'X'
            prev, next = table[cur]
            stack.append([prev, cur, next])
            if next == None:
                cur = table[cur][0]
            else:
                cur = table[cur][1]
            if prev == None:
                table[next][0] = None
            elif next == None:
                table[prev][1] = None
            else:
                table[prev][1] = next
                table[next][0] = prev
        elif c == "Z":
            # 복구
            prev, now, next = stack.pop()
            answer[now] = 'O'
            if prev == None:
                table[next][0] = now
            elif next == None:
                table[prev][1] = now
            else:
                table[next][0] = now
                table[prev][1] = now

        else:
            # 커서 이동
            c1, c2 = c.split(' ')
            c2 = int(c2)
            if c1 == 'D':
                for _ in range(c2):
                    cur = table[cur][1]
            else:
                for _ in range(c2):
                    cur = table[cur][0]
    return ''.join(answer)
```

회고

- 시간 복잡도 문제로 인한 실패
- 기존 그냥 배열을 사용할 경우 insert시 시간복잡도가 n이 걸림
- 이중 링크드리스트는 삽입 del시 시간복잡도 O(1)

실패 코드

```
def solution(n, k, cmds):
    answer = ''
    table = [i for i in range(n)]
    origin_table = [i for i in range(n)]
    removed = []
    cur = k
    for cmd in cmds:
        if cmd[0] == "C":
            item = table.pop(cur)
            removed.append([cur, item])
            if cur == (len(table)):
                cur -= 1
            continue
        if cmd[0] == "Z":
            item = removed.pop(len(removed)-1)
            table.insert(item[0], item[1])
            if item[0] <= cur:
                cur += 1
            continue
        if cmd[0] == "D":
            cmd = cmd.split()
            cur += int(cmd[1])
            if cur > len(table):
                cur = len(table)-1
            continue
        if cmd[0] == "U":
            cmd = cmd.split()
            cur -= int(cmd[1])
            if cur < 0:
                cur = 0
            continue
    cur = 0
    for i in range(len(origin_table)):
        if origin_table[i] != table[cur]:
            answer += "X"
            continue
        answer += "O"
        cur += 1
    return answer

```

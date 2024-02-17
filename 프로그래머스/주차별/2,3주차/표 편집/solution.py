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


solution(8,	2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"])
solution(8, 2,	["D 2", "C", "U 3", "C", "D 4",
         "C", "U 2", "Z", "Z", "U 1", "C"])

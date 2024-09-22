import heapq
from collections import deque

n, m, k = map(int, input().split())

year = 0

# 각 칸 현재 양분
food = [[5]*n for _ in range(n)]

# 겨울에 로봇이 주는 양분
robot = []
for i in range(n):
    robot.append(list(map(int, input().split())))

# 각 칸에 나무의 정보
tree = {}

for i in range(m):
    y, x, age = map(int, input().split())
    y = y-1
    x = x-1
    # 나무 정보 입력
    if not (y, x) in tree:
        tree[(y, x)] = deque()
    tree[(y, x)].append(age)

while year != k:
    # 봄
    # 봄에 양분을 먹지 못한 나무들
    noEatTree = deque()
    addTree = deque()

    for loc, values in tree.items():
        eatTree = deque()
        while values:
            # 양분을 먹은 나무들
            cur = values.popleft()
            if food[loc[0]][loc[1]] >= cur:
                # 양분을 먹었다면 양분 먹은 후 나이
                food[loc[0]][loc[1]] -= cur
                eatTree.append(cur+1)
                if (cur+1) % 5 == 0:
                    addTree.append((loc[0], loc[1]))
            # 이번 순서 나무가 양분을 못먹으면
            else:
                noEatTree.append((loc[0], loc[1], cur))
        tree[(loc[0], loc[1])] = eatTree

    # 여름
    for i, j, age in noEatTree:
        food[i][j] += age // 2

    # 가을
    for y, x in addTree:
        for row in range(-1, 2):
            for col in range(-1, 2):
                if row == 0 and col == 0:
                    continue
                ny = y + row
                nx = x + col
                if ny >= 0 and ny < n and nx >= 0 and nx < n:
                    if not (ny, nx) in tree:
                        tree[(ny, nx)] = deque()
                    tree[(ny, nx)].appendleft(1)

    # 겨울
    for i in range(n):
        for j in range(n):
            food[i][j] += robot[i][j]

    year += 1

count = 0
for value in tree.values():
    count += len(value)
print(count)

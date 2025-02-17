from collections import deque

grid = []
for _ in range(12):
    grid.append(list(input()))


def inBox(i, j):
    return 0 <= i < 12 and 0 <= j < 6


def beq(si, sj):
    q = deque()
    visited = [[0 for _ in range(6)] for _ in range(12)]
    cnt = 0

    q.append((si, sj))
    visited[si][sj] = 1
    cnt += 1

    while q:
        ci, cj = q.popleft()
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = ci + di, cj + dj
            if not inBox(ni, nj) or visited[ni][nj] or grid[ni][nj] != grid[si][sj]:
                continue
            q.append((ni, nj))
            visited[ni][nj] = 1
            cnt += 1

    if cnt >= 4:
        for i in range(12):
            for j in range(6):
                if visited[i][j]:
                    grid[i][j] = '.'
        return True
    else:
        return False


ans = 0
while True:
    # 1. 연쇄
    combo_num = 0
    for i in range(12):
        for j in range(6):
            if grid[i][j] != '.':
                combo_num += beq(i, j)

    # 2. 종료 조건
    if combo_num:
        ans += 1
    else:
        break

    # 3. 중력
    for i in range(11):
        for j in range(6):
            p = i
            while 0 <= p and grid[p][j] != '.' and grid[p + 1][j] == '.':
                grid[p][j], grid[p + 1][j] = grid[p + 1][j], grid[p][j]
                p -= 1
print(ans)
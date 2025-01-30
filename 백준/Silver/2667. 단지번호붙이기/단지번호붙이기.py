from collections import deque

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().strip())))
visited = [[0 for _ in range(N)] for _ in range(N)]


def inBox(i, j, n, m):
    return 0 <= i < n and 0 <= j < m


def beq(si, sj):
    q = deque()

    q.append((si, sj))
    visited[si][sj] = 1
    tmp = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = ci + di, cj + dj
            if not inBox(ni, nj, N, N) or visited[ni][nj] or not arr[ni][nj]:
                continue
            visited[ni][nj] = 1
            tmp += 1
            q.append((ni, nj))

    return tmp

ans = []
for i in range(N):
    for j in range(N):
        if arr[i][j] and not visited[i][j]:
            ans.append(beq(i, j))


print(len(ans))
print(*sorted(ans), sep="\n")


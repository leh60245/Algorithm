import sys
from collections import deque

input = sys.stdin.readline
dist = [(0, 1), (0, -1), (1, 0), (-1, 0)]
ans = 0

N = int(input())
arr = []  # 아님
for _ in range(N):
    s = list(input())
    arr.append(s)
visited = [[0 for _ in range(N)] for _ in range(N)]


def inBox(i, j):
    return 0 <= i < N and 0 <= j < N


def beq(si, sj):
    # 초기 설정
    q = deque()
    visited[si][sj] = 1
    color = arr[si][sj]

    # 시작 설정
    q.append((si, sj))

    while q:
        ci, cj = q.popleft()
        for di, dj in dist:
            ni, nj = ci + di, cj + dj
            if not inBox(ni, nj) or visited[ni][nj] or arr[ni][nj] != color:
                continue
            visited[ni][nj] = 1
            q.append((ni, nj))

    return 0

ans = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            beq(i, j)
            ans += 1
print(ans, end=" ")

for i in range(N):
    for j in range(N):
        if arr[i][j] == "G":
            arr[i][j] = "R"
visited = [[0 for _ in range(N)] for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            beq(i, j)
            ans += 1
print(ans)
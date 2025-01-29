import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(N):
    s = input()[:-1]
    a = []
    for i in s:
        a.append(int(i))
    arr.append(a)
visited = [[0 for _ in range(M)] for _ in range(N)]
dist = [(0, 1), (0, -1), (1, 0), (-1, 0)]
ans = 0

def inBox(i, j):
    return 0 <= i < N and 0 <= j < M

def beq(si, sj):
    # 초기 설정
    q = deque()
    visited[si][sj] = 1

    # 시작 설정
    q.append((si, sj))

    while q:
        ci, cj = q.popleft()
        if (ci, cj) == (N-1, M-1):
            return visited[ci][cj]
        for di, dj in dist:
            ni, nj = ci + di, cj + dj
            if not inBox(ni, nj) or visited[ni][nj] or arr[ni][nj] == 0:
                continue
            visited[ni][nj] = visited[ci][cj] + 1
            q.append((ni, nj))

    return 0

print(beq(0, 0))
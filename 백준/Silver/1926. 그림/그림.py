import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
visited = [[0 for _ in range(M)] for _ in range(N)]
dist = [(0, 1), (0, -1), (1, 0), (-1, 0)]
ans = []

def inBox(i, j):
    return 0 <= i < N and 0 <= j < M

def beq(si, sj):
    # 초기 설정
    q = deque()
    visited[si][sj] = 1
    tmp = 0

    # 시작 설정
    q.append((si, sj))
    tmp += 1

    while q:
        ci, cj = q.pop()
        for di, dj in dist:
            ni, nj = ci + di, cj + dj
            if not inBox(ni, nj) or visited[ni][nj] or arr[ni][nj] == 0:
                continue
            visited[ni][nj] = 1
            tmp += 1
            q.append((ni, nj))

    return tmp

for i in range(N):
    for j in range(M):
        if arr[i][j] and not visited[i][j]:
            ans.append(beq(i, j))

print(len(ans))
if len(ans):
    print(max(ans))
else:
    print(0)
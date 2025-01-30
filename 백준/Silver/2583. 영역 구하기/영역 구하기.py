from collections import deque
M, N, K = map(int, input().split()) # 세로, 가로, 개수
arr = [[0 for _ in range(N)] for _ in range(M)]
visited = [[0 for _ in range(N)] for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    x2, y2 = x2 - 1, y2 - 1
    for i in range(x1, x2+1): # N, 가로
        for j in range(y1, y2+1): # M, 세로
            arr[j][i] = 1

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
            if not inBox(ni, nj, M, N) or visited[ni][nj] or arr[ni][nj]:
                continue
            visited[ni][nj] = 1
            tmp += 1
            q.append((ni, nj))

    return tmp

cnt = 0
sav = []
for i in range(M):
    for j in range(N):
        if not arr[i][j] and not visited[i][j]:
            sav.append(beq(i, j))
            cnt += 1

print(cnt)
print(*sorted(sav))


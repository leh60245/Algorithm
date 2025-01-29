import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split()) # 가로, 세로, 위치 개수
    arr = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K): # 0 <= x < M-1, 0 <= y < N-1
        x, y = map(int, input().split())  # 가로, 세로
        arr[y][x] = 1
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
            for di, dj in dist:
                ni, nj = ci + di, cj + dj
                if not inBox(ni, nj) or visited[ni][nj] or arr[ni][nj] == 0:
                    continue
                visited[ni][nj] = 1
                q.append((ni, nj))

        return 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] and not visited[i][j]:
                beq(i, j)
                ans += 1

    print(ans)
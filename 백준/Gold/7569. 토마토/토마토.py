import sys
from collections import deque

input = sys.stdin.readline
M, N, H = map(int, input().split())
arr = []
for _ in range(H):
    tmp = []
    for _ in range(N):
        s = list(map(int, input().split()))
        tmp.append(s)
    arr.append(tmp)
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
dist = [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]


def inBox(i, j, k):  # 높이, 세로, 가로
    return 0 <= i < H and 0 <= j < N and 0 <= k < M


def beq():
    # 초기 설정
    q = deque()

    # 시작 설정
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 1:
                    q.append((i, j, k))
                    visited[i][j][k] = 1

    while q:
        ci, cj, ck = q.popleft()
        for di, dj, dk in dist:
            ni, nj, nk = ci + di, cj + dj, ck + dk
            if not inBox(ni, nj, nk) or visited[ni][nj][nk] or arr[ni][nj][nk] != 0:
                continue
            visited[ni][nj][nk] = visited[ci][cj][ck] + 1
            q.append((ni, nj, nk))

    return 0

beq()

def answerQ():
    ans = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                # 익어 있지 않은 토마토가 있다면, -1
                if visited[i][j][k] == 0 and arr[i][j][k] == 0:
                    return -1
                ans = max(ans, visited[i][j][k])

    if ans == 1:
        return 0
    else:
        return ans - 1

print(answerQ())
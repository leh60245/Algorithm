import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
arr = []
max_building = 0
for _ in range(N):
    buildings = list(map(int, input().split()))
    arr.append(buildings)
    max_building = max(max(buildings), max_building)


def in_box(i, j):
    return 0 <= i < N and 0 <= j < N


def bfs(si, sj, water):
    # [1] 초기 설정
    q = deque()
    global v

    # [2] 값 입력
    q.append((si, sj))
    v[si][sj] = 1

    # 위치
    while q:
        ci, cj = q.popleft()
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = ci + di, cj + dj
            if in_box(ni, nj) and not v[ni][nj] and arr[ni][nj] > water:
                v[ni][nj] = 1
                q.append((ni, nj))

    return


ans = 1
for water in range(1, max_building):  # 장마 오는 최대 높이
    v = [[0] * N for _ in range(N)]
    safe = 0
    for j in range(N):
        for k in range(N):
            if arr[j][k] > water and not v[j][k]:
                bfs(j, k, water)
                safe += 1
    ans = max(ans, safe)

print(ans)

import sys
from collections import deque

try:
    sys.stdin = open("input3.txt", "r")
except FileNotFoundError:
    pass

input = sys.stdin.readline
K = int(input())
W, H = map(int, input().split())
grid = []
for _ in range(H):
    grid.append(list(map(int, input().split())))

usual = [(0, 1), (0, -1), (1, 0), (-1, 0)]
horse = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]


def bfs(si, sj, sk):
    q = deque()
    v = [[[0 for _ in range(K+1)] for _ in range(W)] for _ in range(H)]

    q.append((si, sj, sk))
    v[si][sj][sk] = 1
    while q:
        ci, cj, ck = q.popleft()
        # 종료 조건
        if (ci, cj) == (H - 1, W - 1):
            return v[ci][cj][ck] - 1
        # 일반 이동
        for di, dj in usual:
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < H and 0 <= nj < W) or grid[ni][nj] or v[ni][nj][ck]:
                continue
            q.append((ni, nj, ck))
            v[ni][nj][ck] = v[ci][cj][ck] + 1
        # 말 이동
        if ck < K:
            for di, dj in horse:
                ni, nj, nk = ci + di, cj + dj, ck + 1
                if not (0 <= ni < H and 0 <= nj < W) or grid[ni][nj] or v[ni][nj][nk]:
                    continue
                q.append((ni, nj, nk))
                v[ni][nj][nk] = v[ci][cj][ck] + 1

    return -1


def main():
    answer = bfs(0, 0, 0)
    print(answer)


if __name__ == "__main__":
    main()

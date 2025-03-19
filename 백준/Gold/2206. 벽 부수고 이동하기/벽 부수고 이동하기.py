import sys
from collections import deque

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass

input = sys.stdin.readline
N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().strip())))


def bfs(si, sj, sk):
    q = deque()
    v = [[[0] * 2 for _ in range(M)] for _ in range(N)]

    q.append((si, sj, sk))
    v[0][0][0] = 1
    while q:
        ci, cj, ck = q.popleft()
        if (ci, cj) == (N - 1, M - 1):
            return min(filter(lambda x: x > 0, v[N - 1][M - 1]))

        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < N and 0 <= nj < M) or v[ni][nj][ck]:
                continue
            if grid[ni][nj]:
                if ck == 0:
                    nk = ck + 1
                else:
                    continue
            else:
                nk = ck
            q.append((ni, nj, nk))
            v[ni][nj][nk] = v[ci][cj][ck] + 1

    return -1


def main():
    print(bfs(0,0,0))


if __name__ == "__main__":
    main()

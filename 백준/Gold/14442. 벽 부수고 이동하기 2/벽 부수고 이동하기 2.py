import sys
from collections import deque

try:
    sys.stdin = open("input2.txt", "r")
except FileNotFoundError:
    pass

input = sys.stdin.readline
n, m, k = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().strip())))


def bfs(si, sj, sk):
    q = deque()
    visited = [[[0 for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]

    q.append((si, sj, sk))
    visited[si][sj][sk] = 1
    while q:
        ci, cj, ck = q.popleft()
        if (ci, cj) == (n - 1, m - 1):
            return visited[ci][cj][ck]
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < n and 0 <= nj < m):
                continue
            if not grid[ni][nj] and not visited[ni][nj][ck]:
                q.append((ni, nj, ck))
                visited[ni][nj][ck] = visited[ci][cj][ck] + 1
            if grid[ni][nj] and ck < k and not visited[ni][nj][ck + 1]:
                q.append((ni, nj, ck + 1))
                visited[ni][nj][ck + 1] = visited[ci][cj][ck] + 1

    return -1


def main():
    print(bfs(0, 0, 0))


if __name__ == "__main__":
    main()

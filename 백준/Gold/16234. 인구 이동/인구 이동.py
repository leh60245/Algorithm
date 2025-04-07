import sys
from collections import deque

DEBUG = False
try:
    sys.stdin = open("example5.txt", "r")
    DEBUG = True
    print()
except FileNotFoundError:
    pass
input = sys.stdin.readline
N, L, R = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))


def bfs(si, sj, v):
    q = deque()
    people = 0
    cnt = 0
    path = list()

    q.append((si, sj))
    v.add((si, sj))
    people += grid[si][sj]
    cnt += 1
    path.append((si, sj))
    while q:
        ci, cj = q.popleft()

        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < N and 0 <= nj < N) or (ni, nj) in v:
                continue
            if L <= abs(grid[ni][nj] - grid[ci][cj]) <= R:
                q.append((ni, nj))
                v.add((ni, nj))
                people += grid[ni][nj]
                cnt += 1
                path.append((ni, nj))

    return people, cnt, path, v

def normalize(p: int, c: int, v: list, g):
    n = p // c
    for i, j in v:
        g[i][j] = n
    return g


def main():
    global grid
    day = 0
    while True:
        un = 0
        visited = set()
        for i in range(N):
            for j in range(N):
                if (i, j) in visited:
                    continue
                people, cnt, path, visited = bfs(i, j, visited)
                grid = normalize(people, cnt, path, grid)
                un += 1


        if un == N * N:
            print(day)
            return
        day += 1



if __name__ == "__main__":
    main()

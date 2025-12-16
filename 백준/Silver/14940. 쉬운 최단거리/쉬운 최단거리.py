import sys
from collections import deque

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass

n, m = map(int, input().split())
grid = list()
start_i, start_j = None, None
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 2:
            start_i, start_j = i, j
    grid.append(line)


def oob(oi, oj):
    return not (0 <= oi < n and 0 <= oj < m)


q = deque()
v = [[-1] * m for _ in range(n)]

q.append((start_i, start_j))
v[start_i][start_j] = 0

while q:
    ci, cj = q.popleft()
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = ci + di, cj + dj
        if oob(ni, nj): continue
        if grid[ni][nj] == 0: continue
        if v[ni][nj] > -1: continue

        q.append((ni, nj))
        v[ni][nj] = v[ci][cj] + 1

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            print(0, end=" ")
        else:
            print(v[i][j], end=" ")
    print()

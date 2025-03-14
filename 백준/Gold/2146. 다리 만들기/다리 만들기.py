import sys
from collections import deque
from itertools import combinations

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass

input = sys.stdin.readline
N = int(input())
grid = []  # 섬은 무조건 2개 이상
for _ in range(N):
    grid.append(list(map(int, input().split())))
land_edge = {}


def bfs(si, sj, visited, num):
    q = deque()
    edge = set()

    q.append((si, sj))
    visited[si][sj] = num
    while q:
        ci, cj = q.popleft()
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < N and 0 <= nj < N) or visited[ni][nj]:
                continue
            if grid[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = num
            else:  # 경계
                edge.add((ni, nj))

    return edge


def cal_bridge(s, e):
    min_len = float('inf')
    for si, sj in land_edge[s]:
        for ei, ej in land_edge[e]:
            min_len = min(abs(si - ei) + abs(sj - ej) + 1, min_len)
    return min_len


def main():
    global land_edge
    # 섬 나누기 & 각 섬의 경계 정보 얻기
    visited = [[0 for _ in range(N)] for _ in range(N)]

    land_number = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] and not visited[i][j]:
                land_number += 1
                edge = bfs(i, j, visited, land_number)
                land_edge[land_number] = edge

    # 각 섬의 경계에서 다른 섬의 경계 연결하기
    bridge = float('inf')

    for two_land in combinations(range(1, land_number + 1), 2):
        start, end = two_land
        bridge = min(cal_bridge(start, end), bridge)

    print(bridge)


if __name__ == "__main__":
    main()

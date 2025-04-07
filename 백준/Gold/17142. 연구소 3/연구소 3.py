import sys
from itertools import combinations
from collections import deque

DEBUG = False
try:
    sys.stdin = open("example8.txt", "r")
    DEBUG = True
    print()
except FileNotFoundError:
    pass
input = sys.stdin.readline
"""
특정 위치에 바이러스 M개 둠
연구소 크기 NxN 정사각형, 
0은 빈칸, 1은 벽, 2는 바이러스 놓을 수 있는 칸
바이러스는 상 하 좌 우 인접한 모든 빈 칸으로 동시에 복제, 1초 걸림

[목표] 모든 빈 칸에 바이러스 퍼질 최소 시간
어떤 방법으로도 모든 빈 칸에 바이러스 못 퍼트리면 -1
"""
N, M = map(int, input().split())  # 크기, 바이러스 개수
# grid = list()
virus_place = list()
walls = set()
for i in range(N):
    line = list(map(int, input().split()))
    for j, value in enumerate(line):
        if value == 1:
            walls.add((i, j))
        elif value == 2:
            virus_place.append((i, j))


def bfs(com):
    q = deque([])
    visited = [[-1 for _ in range(N)] for _ in range(N)]


    for si, sj in com:
        q.append((si, sj))
        visited[si][sj] = 0

    while q:
        ci, cj = q.popleft()
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < N and 0 <= nj < N) or visited[ni][nj] != -1 or (ni, nj) in walls:
                continue
            q.append((ni, nj))
            visited[ni][nj] = visited[ci][cj] + 1
    max_depth = 0
    for i in range(N):
        for j in range(N):
            if (i, j) in virus_place:
                continue
            if visited[i][j] > max_depth:
                max_depth = visited[i][j]

    return max_depth, visited


def check_blank(v):
    for i in range(N):
        for j in range(N):
            if v[i][j] < 0 and (i, j) not in walls and (i, j) not in virus_place:
                return True
    return False


def visual(c, v, com):
    print(f"========== com-{c} ==========")
    for i in range(N):
        for j in range(N):
            if (i, j) in walls:
                print("-", end=" ")
            elif (i, j) in com:
                print("+", end=" ")
            elif (i, j) in virus_place:
                print("x", end=" ")
            elif v[i][j] >= 0:
                print(v[i][j], end=" ")
            else:
                print(0, end=" ")
        print()


def main():
    min_times = -1
    cnt = 1
    for com in combinations(virus_place, M):
        time, visited = bfs(com)

        if not check_blank(visited):
            if min_times == -1:
                min_times = time
            else:
                min_times = min(time, min_times)
        if DEBUG:
            visual(cnt, visited, com)
            print(f"start at {com}")
            print(f"all time {time}")
            cnt += 1
    print(min_times)
    return 0


if __name__ == "__main__":
    main()

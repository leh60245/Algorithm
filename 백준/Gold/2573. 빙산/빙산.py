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
    grid.append(list(map(int, input().split())))


def oob(i, j):
    return not (0 <= i < N and 0 <= j < M)


def melt(i, j):
    height = grid[i][j]
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ni, nj = i + di, j + dj
        if oob(ni, nj) or grid[ni][nj]:
            continue
        height -= 1
    return max(height, 0)

def bfs(si, sj, visited):
    q = deque()

    q.append((si, sj))
    visited[si][sj] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = ci + di, cj + dj
            if oob(ni, nj) or visited[ni][nj] or not grid[ni][nj]:
                continue
            q.append((ni, nj))
            visited[ni][nj] = 1

def check_grid():
    visited = [[0 for _ in range(M)] for _ in range(N)]
    # 첫 번째 빙산을 찾는다.
    find_first = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] and not visited[i][j]:
                if find_first == 0:
                    bfs(i, j, visited)
                    find_first = 1
                else:  # 두 번째 빙산
                    return 2

    return find_first


def main():
    global grid
    is_one = True
    cnt_year = 0
    while True:
        # 빙산 녹이기
        new_grid = [[0 for _ in range(M)] for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if grid[i][j]:
                    new_grid[i][j] = melt(i, j)

        grid = new_grid
        cnt_year += 1

        # 빙산이 두 덩어리 이상으로 분리되는지 확인
        check = check_grid()
        if check == 0:
            print(0)
            return
        elif check == 1:
            continue
        else:  # check_grid() >= 2
            print(cnt_year)
            return cnt_year
    print(cnt_year)
    return

if __name__ == "__main__":
    main()

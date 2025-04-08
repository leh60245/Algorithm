import sys
from collections import deque

DEBUG = False
try:
    sys.stdin = open("example8.txt", "r")
    DEBUG = True
    print()
except FileNotFoundError:
    pass
input = sys.stdin.readline
'''
RxC 격자판, 1x1 크기의 칸, 
공기 청정기는 항상 0-col 위치, 크기는 두 행 차지.
공기 청정기가 설치되어 있지 않은 칸에는 미세먼지가 있고, 양은 Arc

[1초 동안 진행]
1. [미세먼지 확산] 미세먼지 있는 모든 칸에서 동시에 일어남
    r, c에 있는 미세먼지는 인접한 네 방향으로 확산
    인접한 방향에 (1) 공기 청정기가 있거나, (2) 칸이 없으면 -> 그 방향으로 확산이 일어나지 않음
    확산되는 양은 Arc//5 로 소숫점은 버린다.
    (r, c)에 남은 미세먼지 양은 Arc - (Arc//5)x(확산된 방향 개수)이다.
2. [공기 청정기 작동] 
    공기 청정기에서 바람이 나옴
    위쪽 공기청정기의 바람은 '반시계방향'으로 순환, 아래쪽 공기청정기의 바람은 '시계방향'으로 순환
    바람이 불면 -> 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
    공기청정기에서 부는 바람에는 미세먼지 x, 공기청정기로 들어간 미세먼지는 모두 정화
    [사진] 공기 청정기가 있는 행으로 바람이 불고, 벽에 부딛치면 위와 아래로 방향이 돎.
    가장 윗 행과 아랫 행으로부터 두 칸 이상 떨어져있다.
    
[목적] T초가 지난 후 방에 남은 미세먼지 양 출력
'''
R, C, T = map(int, input().split())
grid = []
for _ in range(R):
    grid.append(list(map(int, input().split())))


def spread(grid):
    new_grid = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if grid[i][j] == -1:
                new_grid[i][j] = -1
                continue
            cnt = 0
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if not (0 <= ni < R and 0 <= nj < C) or grid[ni][nj] == -1:
                    continue
                new_grid[ni][nj] += grid[i][j] // 5
                cnt += 1

            tmp = grid[i][j] // 5 * cnt
            new_grid[i][j] += grid[i][j] - tmp

    return new_grid


def rotate_outer_k(grid, k):
    R, C = len(grid), len(grid[0])

    # 1. 외곽 좌표 수집 (시계 방향)
    path = []

    # 상단
    for j in range(C):
        path.append((0, j))
    # 우측
    for i in range(1, R):
        path.append((i, C - 1))
    # 하단
    for j in range(C - 2, -1, -1):
        path.append((R - 1, j))
    # 좌측
    for i in range(R - 2, 0, -1):
        path.append((i, 0))

    # 2. 값 추출
    values = [grid[i][j] for i, j in path]

    # 3. 회전 (시계 방향 → 오른쪽으로)
    dq = deque(values)
    dq.rotate(k)  # 반시계는 dq.rotate(-k)

    # 4. 다시 채워넣기
    for (i, j), v in zip(path, dq):
        grid[i][j] = v

    return grid

def rotate(grid):
    mi = 0
    for i in range(R):
        if grid[i][0] == -1:
            mi = i
            break

    upper_grid = [arr[:] for arr in grid[:mi+1]]
    bottom_grid = [arr[:] for arr in grid[mi+1:]]
    upper_grid = rotate_outer_k(upper_grid, -1)
    bottom_grid = rotate_outer_k(bottom_grid, 1)
    upper_grid[mi][0] = -1
    upper_grid[mi][1] = 0
    bottom_grid[0][0] = -1
    bottom_grid[0][1] = 0

    new_grid = upper_grid+bottom_grid

    return new_grid

def count_dust():
    save = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] > 0:
                save += grid[i][j]
    return save

def visual_grid():
    for i in range(R):
        for j in range(C):
            if grid[i][j] == -1:
                print("*", end=" ")
                continue
            print(grid[i][j], end=" ")
        print()


def main():
    global grid
    if DEBUG:
        visual_grid()
    for t in range(1, T + 1):
        if DEBUG:
            print(f"========= time-{t} ===========")

        grid = spread(grid)
        if DEBUG:
            print(f" [spread] ")
            visual_grid()


        grid = rotate(grid)
        if DEBUG:
            print(f" [rotate] ")
            visual_grid()
            print()

    print(count_dust())


if __name__ == "__main__":
    main()

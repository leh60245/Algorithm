import sys
import copy
DEBUG = False
try:
    sys.stdin = open("example3.txt", "r")
    DEBUG = True
    print()
except FileNotFoundError:
    pass
input = sys.stdin.readline
'''
4x4 격자, 한 칸당 물고기 한 마리 존재. 
각 물고기는 번호와 방향 가짐. 1 <= 번호 <= 16, 같은 번호 없음.
방향은 8가지

[0. 초기] 상어는 (0, 0) 물고기 먹으며 들어옴
상어의 방향은 (0, 0) 물고기의 방향과 동일
그리고 물고기들 모두 이동

[1. 물고기 이동]
번호가 작은 물고기부터 순서대로 이동, 한 칸 이동 가능하며, 
이동은 <빈 칸>, <다른 물고기 있는 칸> /  불가능 <상어칸>, <경계 넘음>
[이동 불가] 각 물고기는 방향이 이동할 수 있는 칸을 향할때까지 방향을 45도 반시계 회전(+1)시킨다.
    만약, 이동할 수 있는 칸이 없으면 -> 이동하지 않는다. 그 외는 이동한다. 
물고기가 다른 물고기가 있는 칸으로 이동시
    -> 서로의 <위치를 바꾸는> 방식으로 이동한다.

[2. 상어 이동]
물고기 이동 모두 끝나면, 상어가 이동한다. 
상어는 방향에 있는 칸으로 이동할 수 있는데, 한 번에 <여러 칸>을 이동할 수 있다.
상어가 물고기가 있는 칸으로 이동했다면
    -> 그 칸의 물고기를 먹고 & 그 물고기의 방향을 가진다.
이동하는 중에 지나는 칸에 있는 물고기는 <먹지 않는다>
물고기가 없는 칸으로 이동할 수 없다. 
[종료] 상어가 이동할 수 있는 칸이 없으면 <공간에서 벗어나 집으로 간다>

[목표] 상어가 먹을 수 있는 물고기 번호의 합의 최댓값을 구해보자.
'''
# (물고기 번호, 방향) x 16
GRID = [[(0, 0) for _ in range(4)] for _ in range(4)]
for x in range(4):
    line = list(map(int, input().split()))
    for y in range(4):
        tmp = line[y * 2:(y + 1) * 2]
        n, d = tmp[0], tmp[1]
        GRID[x][y] = (n, d - 1)
direction = [  # 위에서부터 반시계방향으로 나열
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1)
]
visual_dir = {
    0: '↑',
    1: '↖',
    2: '←',
    3: '↙',
    4: '↓',
    5: '↘',
    6: '→',
    7: '↗'
}

def visual(si, sj, sd, grid):
    for i, line in enumerate(grid):
        for j, info in enumerate(line):
            num, d = info
            if (i, j) == (si, sj):
                print(visual_dir[sd], end=" ")
            else:
                print(num, end=" ")
        print()


def move_fishes(si, sj, grid):
    for number in range(1, 17):
        fish_info = (-1, -1)
        for ci in range(4):
            for cj in range(4):
                if grid[ci][cj][0] == number:
                    fish_info = (ci, cj)
                    break
            if fish_info != (-1, -1):
                break
        if fish_info == (-1, -1):
            continue

        ci, cj = fish_info
        cd = grid[ci][cj][1]
        for dd in range(8):
            nd = (cd + dd) % 8  # 첫 번째는 무조건 기존 방향임
            di, dj = direction[nd]
            ni, nj = ci + di, cj + dj
            # 이동할 수 없으면 다음 방향 확인
            if not (0 <= ni < 4 and 0 <= nj < 4) or (ni, nj) == (si, sj):
                continue
            grid[ni][nj], grid[ci][cj] = (number, nd), grid[ni][nj]
            break
    return grid


max_sum_fishes_number = 0
def dfs(si, sj, grid, score, depth):
    # 점수 계산
    global max_sum_fishes_number
    num, sd = grid[si][sj]
    score += num
    max_sum_fishes_number = max(score, max_sum_fishes_number)
    # 물고기 죽이기 (이때 상어 방향은 저장)
    grid[si][sj] = (0, 0)
    if DEBUG:
        print(f"============= depth {depth} ==============")
        print(f"shark info {(si, sj)}")
        print(f"now eat {score} and all score is {max_sum_fishes_number}")
    # [1 물고기 이동]
    if DEBUG:
        visual(si, sj, sd, grid)
    grid = move_fishes(si, sj, grid)
    if DEBUG:
        print("move fishes")
        visual(si, sj, sd, grid)

    di, dj = direction[sd]
    while True:
        ni, nj = si + di, sj + dj
        if not (0 <= ni < 4 and 0 <= nj < 4) :
            break
        if grid[ni][nj][0] > 0:
            dfs(ni, nj, copy.deepcopy(grid), score, depth+1)
        si, sj = ni, nj
    if DEBUG:
        print("END")
        print()
    return


def main():
    if DEBUG:
        visual(0, 0, 0, GRID)

    dfs(0, 0, GRID, 0, 0)

    print(max_sum_fishes_number)


if __name__ == "__main__":
    main()

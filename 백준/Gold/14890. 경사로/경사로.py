import sys

try:
    sys.stdin = open("example4.txt", "r")
except FileNotFoundError:
    pass
input = sys.stdin.readline
# N*N 지도, 그리고 각 칸엔 높이
# 지도에서 지나갈 수 있는 '길'이 몇 개 있는지 알아본다.
# '길'이란, 한 행 또는 한 열 전부를 나타내며, 한쪽 끝에서 다른쪽 끝까지 지나가는 것이다.

# 길을 지나가는 조건
# 1. 길에 속한 모든 칸의 높이가 '모두 같아야 한다'
# 2. 경사로를 놓아서 지나갈 수 있는 길을 만들 수 있따.
#       ㄴ 경사로는 높이가 항상 1, 길이는 L

# 경사로 조건
# 1. 경사로는 낮은 칸에 놓으며, L 개의 연속된 칸에 경사로의 바닥이 모두 접해야 한다.
# 2. 낮은 칸과 높은 칸의 높이 차이는 1이어야 한다.
# 3. 경사로를 놓을 낮은 칸의 높이는 '모두' 같아야 하고, L개의 칸이 연속되어 있어야 한다.
# 경사로 불가
# 1. 경사로를 놓은 곳에 또 경사로 놓기
# 2. 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
# 3. 낮은 지점의 칸의 높이가 모두 갖지 않거나 or L개가 연속되지 않은 경우
# 4. 경사로를 놓다가 범위를 벗어난 경우

N, L = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]


def rotate(grid):
    new_grid = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_grid[j][N - i - 1] = grid[i][j]
    return new_grid


def count_loads(grid):
    count_loads = 0
    for load in grid:
        can_load = True
        ramps = [0 for _ in range(N)]
        for i in range(N - 1):
            if load[i] == load[i + 1]:
                continue
            elif load[i] - load[i + 1] == 1:
                # 위에서 아래로
                # 그렴 오른쪽 L개가 조건을 만족해야함
                # 1. L개의 연속된 칸 모두 높이가 같음
                # 2. 경사로가 없어야 함
                # 3. 범위를 넘어가지 않음
                base_height = load[i + 1]
                can_ramp = True
                for j in range(1, L + 1):
                    if i + j >= N or ramps[i + j] == 1 or load[i + j] != base_height:
                        can_ramp = False
                        break
                if can_ramp:
                    for j in range(1, L + 1):
                        ramps[i + j] = 1
                else:
                    can_load = False
                    break
            elif load[i] - load[i + 1] == -1:  # 아래에서 위로
                base_height = load[i]
                can_ramp = True
                for j in range(L):
                    if i - j < 0 or ramps[i - j] == 1 or load[i - j] != base_height:
                        can_ramp = False
                        break
                if can_ramp:
                    for j in range(L):
                        ramps[i - j] = 1
                else:
                    can_load = False
                    break
            else:
                can_load = False
                break
        if can_load:
            count_loads += 1
    return count_loads


def main():
    loads = 0
    loads += count_loads(grid)
    r_grid = rotate(grid)
    loads += count_loads(r_grid)
    print(loads)


if __name__ == "__main__":
    main()

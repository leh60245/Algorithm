import sys

try:
    sys.stdin = open("example4.txt", "r")
except FileNotFoundError:
    pass

# start: x, y and all num is 0
# if grid == 0: dice -> grid
# else: grid -> dice and grid = 0
# 주사위를 이동했을 때 마다 up에 쓰여 있는 값을 구하는 프로그램
# 지도 밖으로 이동하는 명령은 무시 및 출력 금지
input = sys.stdin.readline
N, M, ni, nj, K = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))
cmd_list = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]  # bottom, north, east, west, south, up


def oob(i, j):
    return not (0 <= i < N and 0 <= j < M)


def roll(direction):
    global dice
    bottom, north, east, west, south, up = dice
    if direction == 1:  # 동
        dice = [east, north, up, bottom, south, west]
    elif direction == 2:  # 서
        dice = [west, north, bottom, up, south, east]
    elif direction == 4:  # 남
        dice = [south, bottom, east, west, up, north]
    else:  # direction == 3 북
        dice = [north, up, east, west, bottom, south]


dd = {
    1: (0, 1),
    2: (0, -1),
    3: (-1, 0),
    4: (1, 0)
}


def main():
    global ni, nj, grid, dice
    for k in range(K):
        cmd = cmd_list[k]

        # 밖에 나가는지 확인
        di, dj = dd[cmd]
        if oob(ni + di, nj + dj):
            continue
        # 이동하기
        ni, nj = ni + di, nj + dj
        roll(cmd)
        # 계산하기
        if grid[ni][nj] == 0:
            grid[ni][nj] = dice[0]
        else:
            dice[0] = grid[ni][nj]
            grid[ni][nj] = 0
        # 출력하기
        print(dice[-1])

    print()


if __name__ == "__main__":
    main()

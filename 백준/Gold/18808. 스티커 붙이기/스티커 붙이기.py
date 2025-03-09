import sys

# 예제 6번에서 문제 발생
try:
    sys.stdin = open("input8.txt", "r")
except FileNotFoundError:
    pass

input = sys.stdin.readline

N, M, K = map(int, input().split())  # 세로, 가로, 스티커 개수
grid = [[0 for _ in range(M)] for _ in range(N)]
STICKERS = []
for _ in range(K):
    R, C = map(int, input().split())
    tmp = []
    for _ in range(R):
        tmp.append(list(map(int, input().split())))
    STICKERS.append(tmp)


def rotate_sticker_90(sticker):
    n, m = len(sticker), len(sticker[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = sticker[i][j]
    return result


def attach_sticker(si, sj, sticker):
    global grid
    sr, sc = len(sticker), len(sticker[0])
    grid_copy = [i[:] for i in grid]
    for i in range(sr):
        for j in range(sc):
            ni, nj = si + i, sj + j
            if sticker[i][j]:
                if grid[ni][nj]:
                    return False
                else:
                    grid_copy[ni][nj] = 1
    grid = grid_copy
    return True


def attach_sticker_in_grid(sticker):
    sr, sc = len(sticker), len(sticker[0])
    for i in range(N - sr + 1):
        for j in range(M - sc + 1):
            if attach_sticker(i, j, sticker):
                return True

    return False


def main():
    for sticker_number in range(K):
        # 1. 스티커 붙이기.
        sticker = STICKERS[sticker_number]
        rotate_cnt = 0
        while rotate_cnt < 4:
            if attach_sticker_in_grid(sticker):
                break
            # sticker 회전
            sticker = rotate_sticker_90(sticker)
            rotate_cnt += 1

    answer = 0
    for i in range(N):
        answer += sum(grid[i])
    print(answer)


if __name__ == "__main__":
    main()

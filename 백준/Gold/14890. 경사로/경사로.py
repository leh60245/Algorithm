import sys

DEBUG = False
try:
    sys.stdin = open("example2.txt", "r")
    DEBUG = True
    print()
except FileNotFoundError:
    pass
input = sys.stdin.readline
N, L = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]


def rotate(grid):
    new_grid = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_grid[j][N - i - 1] = grid[i][j]
    return new_grid


def check_line(line):
    cnt = 1
    idx = 0
    while idx < len(line) - 1:
        if abs(line[idx] - line[idx + 1]) > 1:
            return False
        if line[idx] == line[idx + 1]:
            cnt += 1
            idx += 1
        elif line[idx] - line[idx + 1] == -1:  # 오르막길
            if cnt < L:
                return False
            cnt = 1
            idx += 1
        else:  # 내리막길
            if idx + L >= N:
                return False
            for i in range(idx + 1, idx + L):
                if line[i] != line[i + 1]:
                    return False
            cnt = 0
            idx += L
    return True


def main():
    loads = 0
    for i, line in enumerate(grid):
        if check_line(line):
            if DEBUG:
                print(f"row number-{i} line is ok")
            loads += 1
    for i, line in enumerate(rotate(grid)):
        if check_line(line):
            if DEBUG:
                print(f"col number-{i} line is ok")
            loads += 1
    print(loads)


if __name__ == "__main__":
    main()

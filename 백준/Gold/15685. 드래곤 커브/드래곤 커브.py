import sys
input = sys.stdin.readline

DEBUG = False
try:
    sys.stdin = open("example4.txt", "r")
    DEBUG = True
except FileNotFoundError:
    pass

N = int(input())
info = [tuple(map(int, input().split())) for _ in range(N)]
grid = [[0] * 101 for _ in range(101)]

# 방향: 0(→), 1(↑), 2(←), 3(↓)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def print_grid():
    for row in grid[:10]:
        print(*row[:10])
    print()

def main():
    for x, y, d, g in info:
        directions = [d]
        for _ in range(g):
            for k in reversed(range(len(directions))):
                directions.append((directions[k] + 1) % 4)

        grid[y][x] = 1  # grid는 [y][x]
        for dir in directions:
            x += dx[dir]
            y += dy[dir]
            if 0 <= x <= 100 and 0 <= y <= 100:
                grid[y][x] = 1
            else:
                break  # 좌표 범위 벗어나면 중단

        if DEBUG:
            print_grid()

    # 1x1 정사각형 카운트
    count = 0
    for i in range(100):
        for j in range(100):
            if grid[i][j] and grid[i][j+1] and grid[i+1][j] and grid[i+1][j+1]:
                count += 1
    print(count)

if __name__ == "__main__":
    main()

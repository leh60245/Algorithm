import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass
input = sys.stdin.readline

grid = []
blanks = []

for i in range(9):
    tmp = input().strip()
    line = []
    for j in range(9):
        if tmp[j] == "0":
            blanks.append((i, j))
        line.append(int(tmp[j]))
    grid.append(line)

rows = [[False for _ in range(10)] for _ in range(9)]
cols = [[False for _ in range(10)] for _ in range(9)]
boxs = [[False for _ in range(10)] for _ in range(9)]

for i in range(9):
    for j in range(9):
        v = grid[i][j]
        if v != 0:
            rows[i][v] = True
            cols[j][v] = True
            boxs[(i // 3) * 3 + (j // 3)][v] = True


def visual_grid():
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end="")
        print()


def backtracking(cnt):
    if cnt == len(blanks):
        visual_grid()
        exit()
        return
    i, j = blanks[cnt]
    for num in range(1, 10):
        if rows[i][num] or cols[j][num] or boxs[(i // 3) * 3 + (j // 3)][num]:
            continue
        rows[i][num] = cols[j][num] = boxs[(i // 3) * 3 + (j // 3)][num] = True
        grid[i][j] = num
        backtracking(cnt + 1)
        grid[i][j] = 0
        rows[i][num] = cols[j][num] = boxs[(i // 3) * 3 + (j // 3)][num] = False


backtracking(0)

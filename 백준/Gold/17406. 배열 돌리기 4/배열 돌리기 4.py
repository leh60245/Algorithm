import sys
from itertools import permutations
import copy
DEBUG = False
try:
    sys.stdin = open("example1.txt", "r")
    DEBUG = True
    print()
except FileNotFoundError:
    pass
input = sys.stdin.readline
'''
크기가 NxM 크기인 배열 A.
배열 A의 값은, '각 행에 있는 모든 수의 합 중 최솟값'을 의미한다.
1 2 3 => 6
2 1 1 => 4
4 5 6 => 15
따라서 배열 A의 값 == 4

배열은 회전 연산 수행할 수 있다. 
r, c, s => 정사각형 시계 방향으로 한 칸씩 돌림

[목표] 배열A와 사용 가능한 회전 연산이 주어졌을 때, 배열 A의 값의 최솟값을 구하자. 
[조건] 회전 연산은 모두 한 번씩 사용해야 하며, 순서는 임의로 정해도 된다.

0 0 0 0 s
0 1 2 3 4
1 0 0 0 


'''
N, M, K = map(int, input().split())
GRID = [list(map(int, input().split())) for _ in range(N)]

cmd_list = []
for _ in range(K):
    r, c, s = map(int, input().split())
    cmd_list.append((r-1, c-1, s))


def rotate_once(grid, r, c, s):
    new_grid = [row[:] for row in grid]
    for layer in range(1, s + 1):
        top = r - layer
        left = c - layer
        bottom = r + layer
        right = c + layer

        # 저장해놓고 한 칸씩 shift
        prev = grid[top][left]
        # 좌측
        for i in range(top+1, bottom+1):
            new_grid[i-1][left] = grid[i][left]
        # 하단
        for j in range(left+1, right+1):
            new_grid[bottom][j-1] = grid[bottom][j]
        # 우측
        for i in range(bottom-1, top-1, -1):
            new_grid[i+1][right] = grid[i][right]
        # 상단
        for j in range(right-1, left-1, -1):
            new_grid[top][j+1] = grid[top][j]

        new_grid[top][left+1] = prev
    return new_grid

def rotate_all(grid, op_seq):
    tmp = copy.deepcopy(grid)
    for r, c, s in op_seq:
        tmp = rotate_once(tmp, r, c, s)
    return tmp

def sum_grid(grid):
    ans = float('inf')
    for line in grid:
        ans = min(ans, sum(line))
    return ans

def visual_grid(grid):
    if not DEBUG:
        return
    for line in grid:
        print(*line)

def dprint(*arg, **kargs):
    if DEBUG:
        print(*arg, **kargs)

def main():
    ans = float('inf')
    cnt = 1
    for perm in permutations(cmd_list):
        dprint(f"======== sol {cnt} =========\n", perm)
        rotated = rotate_all(GRID, perm)
        tmp = sum_grid(rotated)
        ans = min(ans, tmp)
        dprint(f"지금 최솟값 {tmp}, 누적 최솟 값은 {ans}")
        cnt += 1



    print(ans)


if __name__ == "__main__":
    main()

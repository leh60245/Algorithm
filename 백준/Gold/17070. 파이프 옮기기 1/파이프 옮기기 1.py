import sys
from collections import deque

DEBUG = False
try:
    sys.stdin = open("example4.txt", "r")
    DEBUG = True
    print()
except FileNotFoundError:
    pass
input = sys.stdin.readline
'''
NxN 격자, 1번부터 행과 열 시작. 각 칸은 빈칸 또는 벽

파이프는 2개의 연속된 칸을 차지한다. 
1x2, 2x1, 2x2

파이프는 빈 칸만 차지해야 한다.
파이프를 밀 수 있는 방향은 총 3가지 → ↘ ↓
밀면서 회전 시킬 수 있다. 회전은 45도만.
미는 방향은 총 3가지 → ↘ ↓

파이프가
1. 가로로 (1x2)로 놓여졌다면 가능한 이동 방법은 2가지 → ↘
2. 세로로 (2x1)로 놓여졌다면 2가지 ↘ ↓
3. 대각선 (2x2)로 놓여졌다면 3가지 → ↘ ↓
회전하면서 꼭 빈칸이어야 하는 곳이 있다.

처음은 (0,0), (0,1) 차지, 방향은 가로

[목표] 파이프의 한 쪽 끝을 (N,N)으로 이동시키는 방법의 개수를 구하자.
'''
N = int(input())
grid = []
wall = set()
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 1:
            wall.add((i, j))
    grid.append(tmp)
# 가로, 대각선, 세로
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
DIRECTION = [(0, 1), (1, 1), (1, 0)]
CAN_MOVE = [[2, 0], [2, 1], [2, 1, 0]]
CHECK_LIST = {
    0: [(0, 1)],
    1: [(0, 1), (1, 0), (1, 1)],
    2: [(1, 0)]
}
cnt = 0

def visual_grid(grid):
    if not DEBUG:
        return
    for line in grid:
        print(*line)

def main():
    # 처음 위치 저장
    dp[0][1][0] = 1
    # 윗 자리는 모두 가로로만 올 수 있음
    for j in range(2, N):
        if grid[0][j] == 1:
            break
        dp[0][j][0] = dp[0][j-1][0]
    for i in range(1, N):
        for j in range(1, N):
            # 벽이면 돌아가기
            if grid[i][j] == 1:
                continue

            if grid[i][j-1] == 0 and grid[i-1][j] == 0 and grid[i-1][j-1] == 0:
                dp[i][j][1] = sum(dp[i-1][j-1])
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]
            dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2]

    visual_grid(dp)

    print(sum(dp[N-1][N-1]))


if __name__ == "__main__":
    main()

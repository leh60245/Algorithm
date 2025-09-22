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

N = int(input())
board = list()
shark = None  # (row, col, size, eaten)
fishes_count = 0

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 9:
            shark = (i, j, 2, 0)
            row[j] = 0
        elif 0 < row[j] <= 6:
            fishes_count += 1
    board.append(row)


def visual_board(t=None):
    if not DEBUG: return
    print("=" * 10, "time: ", t, "=" * 10)
    print(shark)
    si, sj, _, _ = shark
    for i in range(N):
        for j in range(N):
            if (si, sj) == (i, j):
                print(f"★", end=" ")
            else:
                print(f"{board[i][j]}", end=" ")
        print()
    print()


def bfs():
    global shark, board, fishes_count
    q = deque()
    v = [[0] * N for _ in range(N)]
    dist = N * N
    can_eat_fish = []

    si, sj, ss, se = shark
    q.append((si, sj))
    v[si][sj] = 1
    while q:
        ci, cj = q.popleft()
        # 물고기 죽고, 상어가 먹고, 끝
        if 0 < board[ci][cj] < ss:
            if dist > v[ci][cj] - 1:
                dist = v[ci][cj] - 1
                can_eat_fish = [(ci, cj)]
            elif dist == v[ci][cj] - 1:
                can_eat_fish.append((ci, cj))

        for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < N and 0 <= nj < N) or v[ni][nj] or board[ni][nj] > ss: continue
            q.append((ni, nj))
            v[ni][nj] = v[ci][cj] + 1

    if not can_eat_fish:
        return -1

    can_eat_fish.sort()
    fi, fj = can_eat_fish[0]
    board[fi][fj] = 0
    fishes_count -= 1
    new_eaten = se + 1
    if new_eaten == ss:
        shark = (fi, fj, ss + 1, 0)
    else:
        shark = (fi, fj, ss, new_eaten)
    return dist


def main():
    time = 0
    visual_board(time)
    while True:
        if fishes_count == 0:
            break
        result = bfs()
        if result == -1:
            break
        time += result
        visual_board(time)

    print(time)

    return 0


if __name__ == "__main__":
    main()

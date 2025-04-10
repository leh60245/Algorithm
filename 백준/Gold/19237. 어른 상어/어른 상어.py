import sys

DEBUG = False
try:
    sys.stdin = open("example4.txt", "r")
    DEBUG = True
    print()
except FileNotFoundError:
    pass
input = sys.stdin.readline
'''
상어마다 1~M 번호, 서로 다름
서로 영역을 지키며, 1번 상어가 가장 강력해 나머지를 모두 쫒아냄

[초기]
NxN 크기 격자 중 M개 칸에 상어가 한 마리씩 들어있음
맨 처음에 모든 상어가 자신 위치에 자신 냄새 뿌림
그 후 1초마다 모든 상어가 동시에 상하좌우 인접한 칸 중 하나로 이동하고 자신 냄새 뿌림
냄새는 상어가 k번 이동하고 나면 사라진다.


[상어 움직이기]
각 상어가 이동 방향 결정할 때
1. 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다.
2. 그런 칸이 없으면 
    -> 자신의 냄새가 있는 칸의 방향으로 잡는다. 
이때, 가능한 칸이 여러 개 가능한데, 그 경우 특정한 우선순위를 따른다.

[냄새 선택 우선순위]
우선 순위는 상어마다 다르다. 같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다.
상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고, 
그 후에는 방금 이동한 방향이 보고 있는 방향이 된다.

[모든 상어 이동 후 상어 쫓아내기]
모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있다면,
    -> 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.
    <즉, 가장 작은 번호가 가장 강한 상어다>

[목표] 1번 상어만 격자에 남게 되기까지 몇 초가 걸리는가.
[조건]
맨 처음에는 각 상어마다 빈 칸이 존재한다. 
단, 1,000 초가 넘어도 다른 상어가 격자에 남아 있으면 -1을 출력한다.
'''
# 격자 크기, 상어 수, 냄새가 남는 초
N, M, K = map(int, input().split())

# 위, 아래, 왼쪽, 오른쪽
DIRECTION = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visual_dir = '↑↓←→x'


def visualize_grid(grid):
    for line in grid:
        for n, t in line:
            if t != K:
                print("0", end=" ")
            else:
                print(n, end=" ")
        print()


def visualize_dir(s_d):
    for i in range(1, M + 1):
        if s_d[i] is None:
            print(f"{i}: x", end=" ")
        else:
            print(f"{i}: {visual_dir[s_d[i]]}", end=" ")
    print()


def move_shark(grid, shark_direction, priority):
    new_grid = [[(0, 0) for i in range(N)] for _ in range(N)]
    new_shark_direction = [4] + [None] * M
    dead_count = 0
    for i in range(N):
        for j in range(N):
            # 냄새로 판별. 냄새가 K라면 지금 상어가 거기에 있는 거임
            if grid[i][j][1] == K:
                num, _ = grid[i][j]  # 상어 번호
                new_grid[i][j] = (num, K - 1) if K >= 2 else (0, 0)
                cd = shark_direction[num]  # 상어 현재 방향
                is_blank = False  # 빈칸 여부
                for nd in priority[num][cd]:
                    di, dj = DIRECTION[nd]  # 상어의 다음 방향
                    ni, nj = i + di, j + dj  # 상어의 다음 위치
                    if not (0 <= ni < N and 0 <= nj < N) or grid[ni][nj] != (0, 0):
                        # 경계 밖이거나, 빈칸이 아니라면 다음 위치를 검토한다.
                        continue
                    # 만약 빈칸을 찾았다면,
                    # 그 위치에 넣거나, 더 강한 상어가 살아남는다.
                    is_blank = True
                    if new_grid[ni][nj] == (0, 0):
                        new_grid[ni][nj] = (num, K)
                        new_shark_direction[num] = nd
                    else:
                        next_num, next_time = new_grid[ni][nj]
                        if num > next_num:
                            new_grid[ni][nj] = (next_num, next_time)
                        else:
                            new_grid[ni][nj] = (num, K)
                            new_shark_direction[num] = nd
                        dead_count += 1
                    break

                if is_blank:
                    continue

                # 만약 빈칸이 없었다면, 자기 냄새 쪽으로
                for nd in priority[num][cd]:
                    di, dj = DIRECTION[nd]
                    ni, nj = i + di, j + dj  # 상어의 다음 위치
                    if not (0 <= ni < N and 0 <= nj < N):
                        continue
                    next_num, _ = grid[ni][nj]  # 다음 위치의 상어 번호
                    if next_num == num:  # 다음 위치의 상어 번호가 지금 상어 번호와 동일하다면
                        new_grid[ni][nj] = (num, K)
                        new_shark_direction[num] = nd
                        break
            elif grid[i][j][1] > 1:
                n, t = grid[i][j]
                if new_grid[i][j][1] == K:
                    continue
                new_grid[i][j] = (n, t - 1)

    return new_grid, new_shark_direction, dead_count


def main():
    # 상어 번호, 냄새 남은 시간
    grid = [[(0, 0) for i in range(N)] for _ in range(N)]
    for i in range(N):
        tmp = list(map(int, input().split()))
        for j in range(N):
            if tmp[j] > 0:
                grid[i][j] = (tmp[j], K)
    shark_direction = list(map(int, input().split()))
    shark_direction = [4] + [d - 1 for d in shark_direction]

    priority = {}
    for num in range(1, M + 1):
        priority[num] = {}
        for dddd in range(4):
            tmp = list(map(int, input().split()))
            tmp = [v - 1 for v in tmp]
            priority[num][dddd] = tmp
    if DEBUG:
        print(f"=========== time {0} ==============")
        visualize_grid(grid)
        print(f"shark direction: ", end="")
        visualize_dir(shark_direction)
        print()

    all_dead_shark = 0
    for t in range(1, 1001):
        grid, shark_direction, now_dead = move_shark(grid, shark_direction, priority)
        all_dead_shark += now_dead
        if DEBUG:
            print(f"=========== time {t} ==============")
            visualize_grid(grid)
            print(f"shark direction: ", end="")
            visualize_dir(shark_direction)
            print(f"now dead {now_dead}, all is {all_dead_shark}")
            print()
        if all_dead_shark == M - 1:
            print(t)
            return

    print(-1)
    return


if __name__ == "__main__":
    main()

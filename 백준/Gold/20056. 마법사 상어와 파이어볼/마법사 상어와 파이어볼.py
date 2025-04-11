import sys

DEBUG = False
try:
    sys.stdin = open("example4.txt", "r")
    DEBUG = True
    print()
except FileNotFoundError:
    pass
input = sys.stdin.readline
"""
NxN 격자에 파이어볼 M개를 발사한다.
파이어볼은 각자 위치에서 이동을 대기하고 있다.
i번 파이어볼의 위치는 ri, ci, 질량은 mi, 방향은 di, 속력은 si
격자는 0번행과 N-1행이, 0번 열은 N-1열과 연결되어 있다.
파이어볼의 방향은 인접한 8개의 칸 방향 의미

[이동 명령]
1. 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
    이동하는 중에 같은 칸에 여러 파이어볼이 있을 수 있다.
2. 이동이 모두 끝난 후, 2개 이상의 파이어볼이 있는 칸에 다음 일이 일어난다.
    1) 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
    2) 파이어볼은 4개의 파이어볼로 나누어진다.
3. 나누어진 파이어볼의 질량m, 속력s, 방향d는 다음과 같다.
        1. 질량m = int(M//5)
        2. 속력s = int(S//합쳐진 파이어볼 개수)
        3. 방향이 모두 홀수 or 짝수면 => 짝수 0, 2, 4, 6
            아니면 => 홀수 1, 3, 5, 7
4. [죽음] 질량 0이면 죽는다.
    
[목표] 이동 명령 K번 후, 남아있는 파이어볼 질량의 합을 구하자.
[조건]
4 ≤ N ≤ 50
0 ≤ M ≤ N2
1 ≤ K ≤ 1,000
1 ≤ ri, ci ≤ N
1 ≤ mi ≤ 1,000
1 ≤ si ≤ 1,000
0 ≤ di ≤ 7
"""
N, M, K = map(int, input().split())
DIRECTION = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
vis_dir = "↑↗→↘↓↙←↖"


def visual_grid(grid, label="DEBUG"):
    if not DEBUG:
        return

    print(f"{label}")
    for i in range(N):
        for j in range(N):
            if len(grid[i][j]) >= 2:
                print(f"{len(grid[i][j])}", end=" ")
            elif len(grid[i][j]) == 1:
                _, _, v_d = grid[i][j][0]
                print(f"{vis_dir[v_d]}", end=" ")
            else:
                print(0, end=" ")

        print("||", end=" ")
        for j in range(N):
            sum_m = 0
            for m, s, d in grid[i][j]:
                sum_m += m
            print(sum_m, end=" ")

        print()


def move_fireball(grid):
    new_grid = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not grid[i][j]:
                continue
            for m, s, d in grid[i][j]:
                di, dj = DIRECTION[d]
                ni = (i + di * s) % N
                nj = (j + dj * s) % N
                new_grid[ni][nj].append((m, s, d))

    return new_grid


def sum_and_divide_fireball(grid):
    new_grid = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not grid[i][j]:
                continue
            elif len(grid[i][j]) == 1:
                new_grid[i][j] = grid[i][j]
            else:
                sum_m, sum_s, sum_odd, sum_even = 0, 0, 0, 0
                for m, s, d in grid[i][j]:
                    sum_m += m
                    sum_s += s
                    if d % 2 == 0:
                        sum_even += 1
                    else:
                        sum_odd += 1
                min_m = sum_m // 5
                if min_m <= 0:  # 소멸
                    continue
                min_s = sum_s // len(grid[i][j])
                if sum_odd == 0 or sum_even == 0:
                    min_d = [0, 2, 4, 6]
                else:
                    min_d = [1, 3, 5, 7]
                for m in range(4):
                    new_grid[i][j].append((min_m, min_s, min_d[m]))
    return new_grid

def sum_all_mass(grid):
    an = 0
    for i in range(N):
        for j in range(N):
            for m, _, d in grid[i][j]:
                an += m
    return an

def main():
    grid = [[[] for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        r, c, m, s, d = map(int, input().split())
        r, c = r - 1, c - 1
        grid[r][c].append((m, s, d))
    for k in range(1, K + 1):
        visual_grid(grid, label=f"======== time - {k} ========")
        grid = move_fireball(grid)
        visual_grid(grid, label=">> move fireball")
        grid = sum_and_divide_fireball(grid)
        visual_grid(grid, label=">> sum and divide ball")
        if DEBUG:
            print(sum_all_mass(grid))
            print()
        pass

    print(sum_all_mass(grid))


if __name__ == "__main__":
    main()

import sys
import copy

DEBUG = False
try:
    sys.stdin = open("example5.txt", "r")
    DEBUG = False
    print()
except FileNotFoundError:
    pass
input = sys.stdin.readline
'''
4x4 격자, 물고기 M마리, 이동방향 8개 가짐(상하좌우대각선)
상어도 격자 한 칸에 들어가있음. 
둘 이상 물고기가 같은 칸에 있을 수 있음, 마법사 상어와 물고기가 같이 있을 수 있음

[마법 연습 한 번]
1. 모든 물고기 복제 마법: 시간이 걸리기에 5번에서 물고기가 복제되어 칸에 나타남
2. 모든 물고기가 한 칸 이동: 
    - [이동 불가] 상어가 있는 칸, 물고기 냄새 칸, 격자 범위 밖. 
    - 이동할 수 있는 칸을 향할때까지 방향을 45도 반시계 회전. ( d = d - 1)
    - 만약, 이동할 칸이 없으면 이동 하지 않는다.
    - 그 외의 경우는 그 칸으로 이동한다. 
3. 상어가 연속 3칸 이동한다.
    - 상어는 상 하 좌 우 인접 칸으로 이동 가능하다. (d = 0, 2, 4, 6)
    - 연속해서 이동하는 칸 중에 격자 범위를 벗어나는 칸이 있다면, 그 방법은 불가능한 이동 방법이다.
    - 연속해서 이동 중 물고기가 있는 칸으로 이동하면, 
        -> 그 칸의 모든 물고기는 제외,
        -> 제외되는 모든 물고기는 <냄새>를 남긴다.
    - 가능한 이동 방법 중 제외되는 물고기 수가 가장 많은 방법으로 이동하며, 
        - 그러한 방법이 여러가지인 경우, 사전 순으로 가장 앞서는 방법을 이용한다.
4. 두 번 전 연습에서 생긴 물고기 냄새가 격자에서 사라짐
5. 1에서 사용한 복제 마법 완성. 모든 복제된 물고기는 1에서의 위치와 방향성을 그대로 갖는다.

[사전 순서]
상:0 좌:1 하:2 우:3
앞 - 000, 001, ... , 333 - 뒤
따라서 4444 뒤부터 시작해서 앞으로 이동해보자. 

[목표]
S번의 연습을 마친 후 격자에 있는 물고기의 수를 출력한다.
'''
N = 4
M, S = map(int, input().split())
grid = [[[] for _ in range(N)] for _ in range(N)]
smell = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, dddd = map(int, input().split())
    grid[x - 1][y - 1].append(dddd - 1)

SHARK_DIR = [(-1, 0), (0, -1), (1, 0), (0, 1)]
SHARK_VIS = ["↑", "←", "↓", "→"]
FISH_DIR = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
FISH_VIS = ["←", "↖", "↑", "↗", "→", "↘", "↓", "↙"]

pro_list = list()


def dprint(*args, **kwargs):
    if DEBUG: print(*args, **kwargs)


def visual_grid(emo=True, shark=None):
    if not DEBUG:
        return
    if not emo:
        for i in range(N):
            for j in range(N):
                print(grid[i][j], end=" ")
            print()
        return
    for i in range(N):
        for j in range(N):
            if shark is not None and (i, j) == shark:
                print("x", end=" ")
                continue

            if not grid[i][j]:
                print("□", end=" ")
            elif len(grid[i][j]) == 1:
                print(FISH_VIS[grid[i][j][0]], end=" ")
            else:
                print("■", end=" ")
        print()


def visual_smell():
    if not DEBUG:
        return
    for i in range(N):
        for j in range(N):
            if smell[i][j] == 2:
                print("●", end=" ")
            elif smell[i][j] == 1:
                print('◎', end=" ")
            elif smell[i][j] == 0:
                print('○', end=" ")
        print()


def move_fishes(si, sj):
    new_grid = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not grid[i][j]:
                continue
            for cd in grid[i][j]:
                fish_can_move = False
                for dd in range(8):
                    nd = (cd - dd) % 8
                    di, dj = FISH_DIR[nd]
                    ni, nj = i + di, j + dj
                    if not (0 <= ni < N and 0 <= nj < N) or (ni, nj) == (si, sj) or smell[ni][nj] > 0:
                        continue
                    fish_can_move = True
                    new_grid[ni][nj].append(nd)
                    break
                if not fish_can_move:
                    new_grid[i][j].append(cd)
    return new_grid


max_cnt_fish = -1
save_path_dir = [0, 0, 0]
save_path_idx = []


def move_shark(si, sj, path_dir, path_idx, n, cnt_fish):
    global max_cnt_fish, save_path_dir, save_path_idx
    if len(path_dir) == 0:
        max_cnt_fish = -1
        save_path_dir = [0, 0, 0]
        save_path_idx = []
    if len(path_dir) == n:
        if cnt_fish > max_cnt_fish:
            max_cnt_fish = cnt_fish
            save_path_dir = path_dir
            save_path_idx = path_idx
        return
    for d in range(4):
        di, dj = SHARK_DIR[d]
        ni, nj = si + di, sj + dj
        if not (0 <= ni < N and 0 <= nj < N):
            continue
        if (ni, nj) in path_idx:
            move_shark(ni, nj, path_dir + [d], path_idx + [(ni, nj)], n, cnt_fish)
        else:
            move_shark(ni, nj, path_dir + [d], path_idx + [(ni, nj)], n, cnt_fish + len(grid[ni][nj]))


def min_smell():
    return


def main():
    global grid
    si, sj = map(int, input().split())
    si, sj = si - 1, sj - 1
    dprint(f"init")
    visual_grid(shark=(si, sj))
    # product([0, 1, 2, 3], [], 3)
    for s in range(1, S + 1):
        dprint(f"============ time {s} ===============")
        # 1. 물고기 복제
        dprint(">>>> 1. 물고기 복제")
        copy_grid = copy.deepcopy(grid)
        visual_grid()

        # 2. 물고기 이동
        dprint(">>>> 2. 물고기 이동")
        grid = move_fishes(si, sj)
        visual_grid(emo=False, shark=(si, sj))

        # 3. 상어 이동

        move_shark(si, sj, [], [],3, 0)

        # 물고기 죽이고 냄새 3 남기기
        for pidx in range(3):
            pd = save_path_dir[pidx]
            di, dj = SHARK_DIR[pd]
            si, sj = si + di, sj + dj
            if len(grid[si][sj]) > 0:
                grid[si][sj] = []
                smell[si][sj] = 3

        dprint(">>>> 3. 상어 이동:", save_path_idx)
        visual_grid(shark=(si, sj))

        # 4. 냄새 타이머 줄이기
        for i in range(N):
            for j in range(N):
                smell[i][j] = max(smell[i][j] - 1, 0)
        dprint(">>>> 4. 냄새:")
        visual_smell()

        # 5. 복제 완성
        for i in range(N):
            for j in range(N):
                grid[i][j] = grid[i][j] + copy_grid[i][j]
        dprint(">>>> 5. 물고기 복제:")
        visual_grid(emo=False)
        dprint()

    ans = 0
    for i in range(N):
        for j in range(N):
            ans += len(grid[i][j])
    print(ans)


if __name__ == "__main__":
    main()

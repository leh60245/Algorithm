import sys

DEBUG = False
try:
    sys.stdin = open("example2.txt", "r")
    DEBUG = True
    print()
except FileNotFoundError:
    pass
input = sys.stdin.readline
'''
교실 nxn 크기 격자. 학교 다니는 학생수 N^2
학생은 번호 1~N^2 매겨져 있고, 가장 윗 칸은 (1, 1)

선생은 학생 순서 정했고, 각 학생이 좋아하는 학생 4명도 모두 조사함.
[학생 자리 배정]
1. 비어있는 칸 중 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
2. 1을 만족하는 칸이 여러개라면 -> 인접한 칸 중 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
3. 2를 만족하는 칸이 여러개라면 -> 행 번호가 가장 작은 칸, 그리고 열 번호가 가장 작은 칸으로 자리 정함

[목표]
학생 만족도 구하기. 학생 만족도는 자리 배치 모두 끝난 후에 구할수 있음
그 학생과 긴접한 칸에 앉은 좋아하는 학생 수를 구해야 한다. 
그 값이 0이면 학생 만족도는 0
1이면 1, 2면 10, 3이면 100, 4면 1000 이다. 
'''
N = int(input())
grid = [[0] * N for _ in range(N)]
student_turn = list()
student_like = {}
for _ in range(N * N):
    s, a, b, c, d = map(int, input().split())
    student_turn.append(s)
    student_like[s] = (a, b, c, d)


def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


def visual_grid(grid):
    if not DEBUG:
        return
    for line in grid:
        print(*line)


def check_like_and_blank(s_n, i, j):
    cnt_like, cnt_blank = 0, 0
    for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        ni, nj = i + di, j + dj
        if not (0 <= ni < N and 0 <= nj < N):
            continue
        # 좋아하는 사람이 있는가?
        if grid[ni][nj] in student_like[s_n]:
            cnt_like += 1
            continue
        if not grid[ni][nj]:
            cnt_blank += 1
    return cnt_like, cnt_blank, i, j


def points():
    point = 0
    for i in range(N):
        for j in range(N):
            s_n = grid[i][j]
            s_cnt = 0
            for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                ni, nj = i + di, j + dj
                if not (0 <= ni < N and 0 <= nj < N):
                    continue
                if grid[ni][nj] in student_like[s_n]:
                    s_cnt += 1

            if s_cnt != 0:
                s_point = 10 ** (s_cnt - 1)
                point += s_point
    return point


def main():
    for s_n in student_turn:
        dprint(f"===== 학생 {s_n}번 차례 =====")
        dprint(f"{s_n}번 학생 ♥", student_like[s_n])
        each_gird_info = list()
        for i in range(N):
            for j in range(N):
                if grid[i][j] != 0:
                    continue
                each_gird_info.append(check_like_and_blank(s_n, i, j))
        each_gird_info.sort(key=lambda x: (x[0], x[1], -x[2], -x[3]))
        _, _, ci, cj = each_gird_info[-1]
        grid[ci][cj] = s_n
        visual_grid(grid)
        dprint(f"{s_n}번 학생이 원하는 자리의 정보", each_gird_info[-1])

    ans = points()
    print(ans)


if __name__ == "__main__":
    main()

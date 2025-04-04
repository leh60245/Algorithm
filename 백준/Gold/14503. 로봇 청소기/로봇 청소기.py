import sys

try:
    sys.stdin = open("example2.txt", "r")
except FileNotFoundError:
    pass
input = sys.stdin.readline

# N * M 직사각형, 처음 빈 칸은 모두 청소x, 0=빈칸, 1=벽
# 청소기: 바라보는 방향은 동,서,남,북 중 하나
# 1. 현재 칸 청소x -> 현재 칸 청소
# IF 현재 칸 주변 4칸 중 청소안된빈칸 없으면
#   => 바라보는 방향 유지한 채 한칸 후진 후 1번
#   => 바라보는 방향 뒤에 벽이라면 -> [[작동 멈춤]]
# ELSE 현재 칸 주변 4칸 중 청소안된빈칸 있으면
#   => 반시계 방향 90% 회전
#   => 바라보는 방향 기준 앞쪽 칸 청소X빈칸인 경우 전진
#   => 1번으로
N, M = map(int, input().split())
i, j, d = map(int, input().split())
grid = list()
for _ in range(N):
    grid.append(list(map(int, input().split())))
visited = [[0 for _ in range(M)] for _ in range(N)]
dxy = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]
ans = 0


def dfs(si, sj, sd):
    global ans
    if not visited[si][sj]:
        visited[si][sj] = 1
        ans += 1

    for dd in range(-1, -5, -1):
        nd = (sd + dd) % 4
        di, dj = dxy[nd]
        ni, nj = si + di, sj + dj
        if not grid[ni][nj] and not visited[ni][nj]:
            dfs(ni, nj, nd)
            return

    bd = (sd + 2) % 4
    di, dj = dxy[bd]
    bi, bj = si + di, sj + dj
    if grid[bi][bj]:
        return
    dfs(bi, bj, sd)


def main():
    dfs(i, j, d)
    print(ans)


if __name__ == "__main__":
    main()

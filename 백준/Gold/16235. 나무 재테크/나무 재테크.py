import sys

DEBUG = False
try:
    sys.stdin = open("example8.txt", "r")
    DEBUG = True
    print()
except FileNotFoundError:
    pass
input = sys.stdin.readline
# [봄] '자신의 나이'만큼 양분 먹고, 나이가 +1
# 나무는 자신이 있는 1x1 칸의 양분만 먹을 수 있다.
# 하나의 칸에 여러 나무가 있다면 -> 나이가 어린 나무 부터 먹는다.
# 양분이 부족해, 자신의 나이만큼 양분을 먹을 수 없는 나무는
#   -> !!양분을 먹지 못하고!! 즉시 죽는다. !!!!!
# [여름] 봄에 죽은 나무~> 양분으로 변한다.
# 양분 += 죽은 나무 나이 // 2 (소숫점 아래는 버림)
# [가을] 나무가 번식
# 조건) 번식하는 나무는 나이가 5의 배수
# 인접한 8개 칸 모두에 나이가 1인 나무 생김
# [겨울] 땅에 양분 추가 공급
# 각 칸에 추가되는 양분의 양은 A[r][c]로 입력으로 주어짐

# [목적] K년이 지난 후 땅에 살은 나무 개수 구하기.
N, M, K = map(int, input().split())  # N 크기의 땅, M개 나무, K년
grid = [[5 for _ in range(N)] for _ in range(N)]
A = list()
for _ in range(N):
    A.append(list(map(int, input().split())))
trees = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    i, j, y = map(int, input().split())
    i, j = i - 1, j - 1
    trees[i][j].append(y)
for i in range(N):
    for j in range(N):
        trees[i][j].sort()


def visual():
    for line in grid:
        print(" ".join(map(str, line)))


def count_trees():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                cnt += len(trees[i][j])
    return cnt


def main():
    global grid, trees
    for _ in range(K):
        # 봄
        dead_trees = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if not trees[i][j]:
                    continue
                grow_trees = list()
                for y in trees[i][j]:
                    if grid[i][j] >= y:
                        grid[i][j] -= y
                        grow_trees.append(y + 1)
                    else:
                        dead_trees[i][j] += y // 2

                trees[i][j] = grow_trees

        # 여름
        for i in range(N):
            for j in range(N):
                if dead_trees[i][j]:
                    grid[i][j] += dead_trees[i][j]

        # 가을
        for i in range(N):
            for j in range(N):
                if not trees[i][j]:
                    continue
                for y in trees[i][j]:
                    if not y % 5 == 0:
                        continue
                    for di, dj in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
                        ni, nj = i + di, j + dj
                        if not (0 <= ni < N and 0 <= nj < N):
                            continue
                        trees[ni][nj] = [1] + trees[ni][nj]

        # 겨울
        for i in range(N):
            for j in range(N):
                grid[i][j] += A[i][j]

        if DEBUG:
            visual()

    print(count_trees())


if __name__ == "__main__":
    main()

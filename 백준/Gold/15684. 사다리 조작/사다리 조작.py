import sys

DEBUG = False
try:
    sys.stdin = open("example6.txt", "r")
    DEBUG = True
    print()
except FileNotFoundError:
    pass
input = sys.stdin.readline
N, M, H = map(int, input().split())
ladders = set()
for _ in range(M):
    a, b = map(int, input().split())
    ladders.add((a - 1, b - 1))
answer = 4


def can_place(i, j):
    return (
            (i, j) not in ladders and
            (i, j - 1) not in ladders and
            (i, j + 1) not in ladders
    )


def simulate():
    for col in range(N):
        row, point = 0, col
        while row < H:
            if (row, point) in ladders:
                point += 1
            elif (row, point - 1) in ladders:
                point -= 1
            row += 1
        if point != col:
            if DEBUG:
                print(f"col {col + 1} -> {point + 1} {'x' if col != point else 'o'}")
            return False
    return True


def dfs(depth, si, sj):
    global answer
    if depth >= answer:
        return
    if simulate():
        answer = depth
        return
    if depth == 3:
        return
    for i in range(si, H):
        j_start = sj if i == si else 0
        for j in range(j_start, N - 1):  # 나와 내 오른쪽 확인
            if not can_place(i, j):
                continue
            ladders.add((i, j))
            dfs(depth + 1, i, j)
            ladders.remove((i, j))
        sj = 0


def main():
    dfs(0, 0, 0)
    if answer == 4:
        print(-1)
    else:
        print(answer)


if __name__ == "__main__":
    main()

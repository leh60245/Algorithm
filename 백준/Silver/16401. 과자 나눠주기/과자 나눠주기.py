import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass
input = sys.stdin.readline

M, N = map(int, input().split())
snack = sorted(list(map(int, input().split())))


def search():
    st = 1
    en = snack[-1]
    ans = 0

    while st <= en:
        mid = (st + en) // 2
        cnt = 0
        for value in snack:
            cnt += value // mid
        if cnt >= M:
            ans = mid
            st = mid + 1
        elif cnt < M:
            en = mid - 1

    return ans

print(search())
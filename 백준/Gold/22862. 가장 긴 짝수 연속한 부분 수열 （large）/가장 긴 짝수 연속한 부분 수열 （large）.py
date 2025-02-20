import sys


def foo(n, k, arr):
    ans = 0
    can_delete = k + 1
    tmp = 0

    en = 0
    for st in range(n):
        while en < n and can_delete > 0:
            if arr[en] % 2 == 0:
                tmp += 1
            else:
                can_delete -= 1
            en += 1

        ans = max(ans, tmp)

        if arr[st] % 2 == 0:
            tmp -= 1
        else:
            can_delete += 1

    return ans


if __name__ == "__main__":
    try:
        sys.stdin = open("input.txt", "r")
    except FileNotFoundError:
        pass

    input = sys.stdin.readline

    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    print(foo(n, k, arr))

import sys


def foo(n, arr):
    ans = 0
    seen = set()

    en = 0
    for st in range(n):
        while en < n and arr[en] not in seen:
            seen.add(arr[en])
            en += 1
        ans += en - st
        seen.remove(arr[st])

    return ans


if __name__ == "__main__":
    try:
        sys.stdin = open("input.txt", "r")
    except FileNotFoundError:
        pass

    input = sys.stdin.readline

    n = int(input())
    arr = list(map(int, input().split()))

    print(foo(n, arr))

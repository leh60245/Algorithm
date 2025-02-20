import sys
from collections import deque


def foo(n, k):
    ans = []
    dq = deque(range(1, n + 1))

    while dq:
        dq.rotate(-(k - 1))
        ans.append(dq.popleft())

    return "<" + ", ".join(map(str, ans)) + ">"


if __name__ == "__main__":
    try:
        sys.stdin = open("input.txt", "r")
    except FileNotFoundError:
        pass

    input = sys.stdin.readline

    n, k = map(int, input().split())

    print(foo(n, k))

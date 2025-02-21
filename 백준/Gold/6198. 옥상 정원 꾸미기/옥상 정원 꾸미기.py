import sys
from collections import deque


def foo(n, arr):
    stack = deque()

    ans = 0
    for i in arr:
        if not stack:
            stack.append(i)
            continue
        if stack[-1] > i:
            ans += len(stack)
            stack.append(i)
            continue
        while stack:
            stack.pop()
            if stack and stack[-1] > i:
                break
        ans += len(stack)
        stack.append(i)
    return ans


if __name__ == "__main__":
    try:
        sys.stdin = open("input.txt", "r")
    except FileNotFoundError:
        pass

    input = sys.stdin.readline

    n = int(input())
    arr = [int(input()) for _ in range(n)]

    print(foo(n, arr))

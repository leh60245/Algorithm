import sys
from collections import deque

def unique_combinations_recursive(arr, length):
    result = []

    def backtrack(start, path):
        if len(path) == length:
            result.append(tuple(path))
            return
        for i in range(start, len(arr)):
            backtrack(i + 1, path + [arr[i]])

    backtrack(0, [])
    return result


def foo(n, m, arr):
    ans = 0

    all_result = unique_combinations_recursive(arr, 3)
    for r in all_result:
        tmp = sum(r)
        if tmp < m:
            ans = max(ans, tmp)
        elif tmp == m:
            ans = tmp
            break

    return ans


if __name__ == "__main__":
    try:
        sys.stdin = open("input.txt", "r")
    except FileNotFoundError:
        pass

    input = sys.stdin.readline

    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    print(foo(n, m, arr))

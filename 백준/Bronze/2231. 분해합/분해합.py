import sys


def foo(n):
    """가장 작은 생성자를 찾는 함수"""
    start = max(1, n - 9 * len(str(n)))  # 가능한 생성자의 최소값
    for m in range(start, n):  # start부터 n까지 탐색
        if m + sum(map(int, str(m))) == n:
            return m
    return 0  # 생성자가 없는 경우


if __name__ == "__main__":
    try:
        sys.stdin = open("input.txt", "r")
    except FileNotFoundError:
        pass

    input = sys.stdin.readline

    n = int(input())

    print(foo(n))

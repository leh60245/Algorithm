import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass

input = sys.stdin.readline
N, M = map(int, input().split())


def backtracking(path):
    if len(path) == M:
        print(*path)
        return
    for i in range(N):
        backtracking(path + [i + 1])


def main():
    backtracking([])


if __name__ == "__main__":
    main()

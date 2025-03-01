import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass

input = sys.stdin.readline
N, M = map(int, input().split())


def backtracking(start_idx, path):
    if len(path) == M:
        print(*path)
        return
    for i in range(start_idx, N):
        backtracking(i + 1, path + [i + 1])


def main():
    backtracking(0, [])


if __name__ == "__main__":
    main()

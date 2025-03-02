import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
result = [0 for _ in range(M)]


def backtracking(cnt):
    if cnt == M:
        print(*result)
        return
    start = 0 if cnt == 0 else result[cnt-1] - 1
    for i in range(start, N):
        result[cnt] = i+1
        backtracking(cnt+1)


def main():
    backtracking(0)


if __name__ == "__main__":
    main()

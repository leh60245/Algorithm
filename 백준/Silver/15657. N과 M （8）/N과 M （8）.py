import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass

input = sys.stdin.readline
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = [0 for _ in range(M)]


def backtracking(start, cnt):
    if cnt == M:
        print(*result)
        return
    for i in range(start, N):
        if cnt > 0 and arr[i] < result[cnt-1]:
            continue
        result[cnt] = arr[i]
        backtracking(start, cnt + 1)


def main():
    backtracking(0, 0)


if __name__ == "__main__":
    main()

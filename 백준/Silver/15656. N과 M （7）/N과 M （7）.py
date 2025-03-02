import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass

input = sys.stdin.readline
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = [0 for _ in range(M)]



def backtracking(cnt):
    if cnt == M:
        print(*result)
        return
    for i in range(N):
        result[cnt] = arr[i]
        backtracking(cnt + 1)


def main():
    backtracking(0)


if __name__ == "__main__":
    main()

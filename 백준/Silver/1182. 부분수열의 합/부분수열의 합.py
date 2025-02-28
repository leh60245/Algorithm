import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass

input = sys.stdin.readline
N, S = map(int, input().split())
ARR = list(map(int, input().split()))
ans = 0


def backtracking(cnt, total):
    global ans
    if cnt == N:
        if total == S:
            ans += 1
        return
    backtracking(cnt + 1, total)
    backtracking(cnt + 1, total + ARR[cnt])


def main():
    global ans
    backtracking(0, 0)
    if S == 0:
        ans -= 1
    print(ans)


if __name__ == "__main__":
    main()

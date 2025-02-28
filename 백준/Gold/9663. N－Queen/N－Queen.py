import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass

input = sys.stdin.readline
n = int(input())
ans = 0
isused1 = [False for _ in range(n)]
isused2 = [False for _ in range(2 * n - 1)]
isused3 = [False for _ in range(2 * n - 1)]


def backtracking(cnt):
    global ans
    if cnt == n:
        ans += 1
        return
    for i in range(n):
        if isused1[i] or isused2[i+cnt] or isused3[cnt-i+n-1]:
            continue
        isused1[i] = True
        isused2[i+cnt] = True
        isused3[cnt-i+n-1] = True
        backtracking(cnt+1)
        isused1[i] = False
        isused2[i + cnt] = False
        isused3[cnt - i + n - 1] = False

def main():
    backtracking(0)
    print(ans)

if __name__ == "__main__":
    main()

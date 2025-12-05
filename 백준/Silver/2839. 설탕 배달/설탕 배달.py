import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass
input = sys.stdin.readline

N = int(input())

dp = [-1] * (N+1)
dp[0] = 0
for i in range(1, N+1):
    if i < 3:
        continue
    elif 3 <= i < 5:
        if dp[i-3] >= 0:
            dp[i] = dp[i-3] + 1
    else:
        if dp[i-3] >= 0 and dp[i-5] >= 0:
            dp[i] = min(dp[i-3] + 1, dp[i-5] + 1)
        elif dp[i-3] >= 0:
            dp[i] = dp[i-3] + 1
        elif dp[i-5] >= 0:
            dp[i] = dp[i-5] + 1

print(dp[N])
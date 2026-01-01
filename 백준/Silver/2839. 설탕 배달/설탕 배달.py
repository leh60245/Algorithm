import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass

n = int(input())

dp = [5001] * (n+1)
dp[3] = 1
if n >= 5:
    dp[5] = 1

for idx in range(6, n+1):
    dp[idx] = min([dp[idx], dp[idx-3] + 1, dp[idx-5] + 1])

if dp[n] == 5001:
    print(-1)
else:
    print(dp[n])
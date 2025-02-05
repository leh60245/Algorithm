N = int(input())

# [i번 자리에 0을 사용, i번 자리에 1을 사용]
dp = [[0, 0] for _ in range(N)]
dp[0] = [0, 1]

for i in range(1, N):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]

print(sum(dp[N-1]))

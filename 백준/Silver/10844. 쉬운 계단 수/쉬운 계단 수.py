N = int(input())

dp = [[0 for _ in range(10)] for _ in range(N+1)]
dp[1] = [0] + [1 for _ in range(9)]

for i in range(2, N+1):
    for j in range(10):
        if 1 <= j <= 8:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        elif j < 1:
            dp[i][j] = dp[i-1][j+1]
        else:
            dp[i][j] = dp[i-1][j-1]



print(sum(dp[N]) % 1000000000)


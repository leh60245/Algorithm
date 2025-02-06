T = int(input())
dp = [0] * 101
dp[1], dp[2], dp[3], dp[4], dp[5] = 1, 1, 1, 2, 2
for _ in range(T):
    n = int(input())
    for i in range(6, n+1):
        if dp[i] != 0:
            continue
        dp[i] = dp[i-1] + dp[i-5]
    print(dp[n])

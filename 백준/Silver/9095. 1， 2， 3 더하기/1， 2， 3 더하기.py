T = int(input())
arr = []
dp = [None] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4


for _ in range(T):
    N = int(input())
    for i in range(4, N+1):
        if dp[i] is not None:
            continue
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[N])
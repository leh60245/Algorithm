N = int(input())
dp = [0] * (N+2)
for day in range(1, N+1):
    time, price = map(int, input().split())
    dp[day] = max(dp[day-1], dp[day])

    if day + time <= N+1:
        dp[day + time] = max(dp[day] + price, dp[day + time])

print(max(dp))
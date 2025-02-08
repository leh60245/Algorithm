N = int(input())

if N == 0:
    print(0)
    exit()

podos = [0] + [int(input()) for _ in range(N)]  # 1-based index 유지
dp = [0] * (N + 1)

dp[1] = podos[1]
if N > 1:
    dp[2] = podos[1] + podos[2]

if N >= 3:
    for i in range(3, N+1):
        dp[i] = max(dp[i-1], dp[i-2] + podos[i], dp[i-3] + podos[i-1] + podos[i])

print(dp[N])

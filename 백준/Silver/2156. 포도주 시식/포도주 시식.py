N = int(input())

podos = []
for _ in range(N):
    podos.append(int(input()))

if N <= 2:
    print(sum(podos))
    exit()


dp = [0] * N
dp[0] = podos[0]
dp[1] = podos[0] + podos[1]



for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2] + podos[i], dp[i-3] + podos[i-1] + podos[i])

print(dp[N-1])
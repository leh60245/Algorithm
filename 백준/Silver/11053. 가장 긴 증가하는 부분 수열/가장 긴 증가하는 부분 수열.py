N = int(input()) # 1 <= N <= 1000
arr = list(map(int, input().split())) # 1 <= x <= 1000

dp = [1] * N


for i in range(N):
    for j in range(i):
        # 순차적으로 선택
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
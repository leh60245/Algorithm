N = int(input()) # 1 <= N <= 1000
arr = list(map(int, input().split())) # 1 <= x <= 1000

dp = arr.copy()

# 0 <= j < i < N
for i in range(N):
    for j in range(i):
        # 순차적으로 선택
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))
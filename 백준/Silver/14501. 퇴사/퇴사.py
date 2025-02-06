N = int(input()) # 1 <= N <= 15
dp = [0] * (N+2) # i번째 날에 상담을 시작했을 때 얻을 수 있는 최대 수익
times = [0]
price = [0]
for _ in range(N):
    t, p = map(int, input().split())
    times.append(t)
    price.append(p)

for day in range(N, 0, -1):
    if day + times[day] > N + 1:  # 날짜를 지남
        dp[day] = dp[day+1]
    else: # 날짜 안
        dp[day] = max(dp[day + times[day]] + price[day], dp[day+1])

print(max(dp))
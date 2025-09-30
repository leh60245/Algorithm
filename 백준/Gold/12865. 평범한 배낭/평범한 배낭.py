n, k = map(int, input().split())  # 최대 허용 무게
weight = list()
value = list()
for _ in range(n):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

dp = [0] * (k + 1)

for i in range(n):
    for w in range(k, weight[i] - 1, -1):
        dp[w] = max(dp[w], dp[w - weight[i]] + value[i])

print(max(dp))

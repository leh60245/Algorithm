T = int(input())
dp = [0] * 41
dp[0] = 0
dp[1] = 1
pre = [[0, 0] for _ in range(41)]
pre[0] = [1, 0]
pre[1] = [0, 1]


def fibonacci(n):
    if n == 0:
        return 1, 0
    if n == 1:
        return 0, 1
    a, b = fibonacci(n - 1)
    c, d = fibonacci(n - 2)
    return a + c, b + d


for _ in range(T):
    N = int(input())
    if N == 0 or N == 1:
        print(*pre[N])
        continue
    for i in range(2, N + 1):
        if dp[i]:
            continue
        dp[i] = dp[i - 1] + dp[i - 2]
        pre[i] = [pre[i - 1][0] + pre[i - 2][0],
                  pre[i - 1][1] + pre[i - 2][1]]

    print(*pre[N])

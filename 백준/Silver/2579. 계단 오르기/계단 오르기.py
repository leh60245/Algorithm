T = int(input())
score = [0]
for _ in range(T):
    score.append(int(input()))



def foo():
    if T <= 2:

        return sum(score[:T+1])
    dp = [0] * (T+1)
    dp[1] = score[1]
    dp[2] = score[2]
    dp[3] = score[3]

    for i in range(3, T+1):
        dp[i] = score[i] + min(dp[i-2], dp[i-3])

    return sum(score) - min(dp[T-2], dp[T-1])

print(foo())
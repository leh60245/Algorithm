A = list(map(int, input().split()))
B = list(map(int, input().split()))
S= sum(A)
T = sum(B)
ans = S if S >= T else T
print(ans)

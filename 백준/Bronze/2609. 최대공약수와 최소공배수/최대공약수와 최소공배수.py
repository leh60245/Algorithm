n, m = map(int, input().split())
tmp = min(n, m)
i = tmp
for i in range(tmp, 0, -1):
    if n % i == 0 and m % i == 0:
        break
print(i)
print(n * (m//i))
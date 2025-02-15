n, m = map(int, input().split())
primes = []
for i in range(2, m+1):
    isPrime = True
    for p in primes:
        if p * p > i: break
        if i % p == 0:
            isPrime = False
            break
    if isPrime: primes.append(i)


for p in primes:
    if p < n: continue
    print(p)
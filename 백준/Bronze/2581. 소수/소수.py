import sys

def is_prime(x: int) -> bool:
    if x < 2:
        return False
    # 2부터 sqrt(x)까지 나누어 떨어지는지 확인
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

def main():
    input = sys.stdin.readline
    M = int(input().strip())
    N = int(input().strip())

    primes = []
    for num in range(M, N + 1):
        if is_prime(num):
            primes.append(num)

    if not primes:
        print(-1)
    else:
        print(sum(primes))
        print(min(primes))

if __name__ == "__main__":
    main()

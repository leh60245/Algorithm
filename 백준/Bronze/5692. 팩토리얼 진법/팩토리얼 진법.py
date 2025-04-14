import sys
input = sys.stdin.readline

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def factorial_base_to_decimal(s):
    total = 0
    for i, digit in enumerate(reversed(s)):
        total += int(digit) * factorial(i + 1)
    return total

def main():
    while True:
        line = input().strip()
        if line == "0":
            break
        print(factorial_base_to_decimal(line))

if __name__ == "__main__":
    main()

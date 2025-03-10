import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass

input = sys.stdin.readline


def main():
    while True:
        m, n = map(int, input().split())
        if m == 0 and n == 0:
            break
        if n >= m and n % m == 0:
            print("factor")
        elif n < m and m % n == 0:
            print("multiple")
        else:
            print("neither")



if __name__ == "__main__":
    main()

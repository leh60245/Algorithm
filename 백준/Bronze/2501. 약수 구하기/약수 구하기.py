import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass

input = sys.stdin.readline


def main():
    n, k = map(int, input().split())
    for i in range(1, n+1):
        if n % i == 0:
            k -= 1
            if k == 0:
                print(i)
                return

    print(0)
    return


if __name__ == "__main__":
    main()

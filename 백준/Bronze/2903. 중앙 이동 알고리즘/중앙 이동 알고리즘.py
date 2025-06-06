import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass


def main():
    N = int(input())
    arr = [0 for i in range(16)]
    b = 1
    a = 2
    for i in range(1, 16):
        a += b
        arr[i] = pow(a, 2)
        b *= 2
    print(arr[N])


if __name__ == "__main__":
    main()

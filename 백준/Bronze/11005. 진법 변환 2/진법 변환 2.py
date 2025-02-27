import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass

input = sys.stdin.readline


def main():
    n, b = map(int, input().split())
    ans = []
    while n:
        tmp = n % b
        if tmp >= 10:
            tmp = chr(55+tmp)
        ans.append(tmp)
        n //= b
    print("".join(map(str, ans[::-1])))

if __name__ == "__main__":
    main()

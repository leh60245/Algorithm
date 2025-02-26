import sys


def main():
    n = int(input())
    answer = -1
    for y in range(n + 1, 10000):
        a, b = y // 100, y % 100
        c = (a + b) ** 2
        if y == c:
            answer = y
            break
    print(answer)


if __name__ == '__main__':
    main()

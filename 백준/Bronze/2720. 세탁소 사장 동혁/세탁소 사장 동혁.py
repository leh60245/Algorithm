import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass
input = sys.stdin.readline

T = int(input())
money = [25, 10, 5, 1]

for _ in range(T):
    N = int(input())
    for m in money:
        tmp = N // m
        print(tmp, end=" ")
        N = N % m
    print()
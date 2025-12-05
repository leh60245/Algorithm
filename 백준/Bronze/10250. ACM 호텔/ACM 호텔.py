import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    h = N % H if N % H != 0 else H
    print(h, end="")
    w = (N-1) // H + 1
    w = str(w) if w >= 10 else "0" + str(w)
    print(w)

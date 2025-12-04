import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass
input = sys.stdin.readline

tmp = list(map(int, input().split()))
if tmp == [v for v in range(1, 9)]:
    print("ascending")
elif tmp == [v for v in range(8, 0, -1)]:
    print("descending")
else:
    print("mixed")
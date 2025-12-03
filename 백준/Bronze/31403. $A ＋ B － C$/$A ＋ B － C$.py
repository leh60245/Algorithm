import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
print(a+b-c)
print(int(str(a) + str(b)) - c)

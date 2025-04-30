n, m = map(int, input().split())
for _ in range(n):
    line = list(input())
    print("".join(map(str, line[::-1])))
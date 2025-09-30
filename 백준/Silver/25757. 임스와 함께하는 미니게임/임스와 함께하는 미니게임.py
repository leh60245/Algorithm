n, t = map(str, input().split())
n = int(n)
t = 1 if t == "Y" else 2 if t == "F" else 3

names = set()
for _ in range(n):
    names.add(input())

print(len(names) // t)
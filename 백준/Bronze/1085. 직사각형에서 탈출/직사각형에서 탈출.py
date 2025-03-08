x, y, w, h = map(int, input().split())
answer = min(min(x, w-x), min(y, h-y))
print(answer)
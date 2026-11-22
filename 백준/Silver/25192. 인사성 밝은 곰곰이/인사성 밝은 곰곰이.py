answer = 0
N = int(input())
history = set()
while N:
    cmd = input()
    if cmd == "ENTER":
        history = set()
    else:
        if cmd not in history:
            history.add(cmd)
            answer += 1
    N -= 1

print(answer)

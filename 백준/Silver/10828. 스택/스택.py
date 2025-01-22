n = int(input())    # 명령어의 수
dir = []            # 명령어를 담을 배열열
answer = []
for _ in range(n):
    instruction = list(map(str, input().split()))
    if instruction[0] == "push":
        num = int(instruction[1])
        dir.append(num)
    elif instruction[0] == "pop":
        if dir == []:
            answer.append(-1)
            continue
        answer.append(dir[-1])
        dir = dir[:-1]
    elif instruction[0] == "size":
        answer.append(len(dir))
    elif instruction[0] == "empty":
        if dir == []:
            answer.append(1)
        else:
            answer.append(0)
    else:
        if dir == []:
            answer.append(-1)
            continue
        answer.append(dir[-1])

for i in answer:
    print(i)   
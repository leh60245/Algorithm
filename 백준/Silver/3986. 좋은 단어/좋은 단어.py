n = int(input())
cnt = 0
for _ in range(n):
    a = input()
    stack = []
    
    if len(a) % 2 == 1:
        continue
    
    stack.append(a[0])
    a = a[1:]
    for i in a:
        if not stack or i != stack[-1]:
            stack.append(i)
        else:
            stack.pop()
            
    if stack == []:
        cnt += 1
    else:
        continue

print(cnt)
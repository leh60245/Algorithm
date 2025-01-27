n = int(input())

for _ in range(n):
    a = input()    
    if len(a) % 2 == 1 or a[0] == ")" or a[-1] == '(':
        print("NO")
        continue
    
    stack = []
    stack.append(a[0])
    a = a[1:]
    no_err = 1
    for i in a:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                no_err = 0
                break
            stack.pop()
            
    if no_err and stack == []:
        print("YES")
    else:
        print("NO")

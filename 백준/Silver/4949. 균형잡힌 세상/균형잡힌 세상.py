import sys
from collections import deque
input = sys.stdin.readline

while True:
    cmd = input()[:-1]
    if cmd == '.':
        break

    stack = []
    p = 0
    isAnswer = True
    while cmd[p] != '.':
        i = cmd[p]
        p += 1
        if not (i == '(' or i =='[' or i == ')' or i == ']'):
            continue
        # stack이 비어 있음
        if stack == [] and (i == '(' or i == '['):
            stack.append(i)
            continue

        if i == '(' or i == '[':
            stack.append(i)
            continue

        if i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                isAnswer = False
                break

        if i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                isAnswer = False
                break

    if not isAnswer or stack:
        print('no')
    else:
        print('yes')
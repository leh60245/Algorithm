import sys
from collections import deque
input = sys.stdin.readline

arr = input()[:-1]
stack = deque([])


answer = 0

for idx in range(len(arr)):
    if arr[idx] == "(":
        stack.append("(")
    else:   # i == ")"
        if arr[idx-1] == "(":    # layzer
            answer += len(stack) - 1
            stack.pop()
        else: # the edge of the top stick
            answer += 1
            stack.pop()

print(answer)
import sys

DEBUG = False
try:
    sys.stdin = open("example6.txt", "r")
    DEBUG = True
    print()
except FileNotFoundError:
    pass
input = sys.stdin.readline
'''
길이가 N인 수식이 있다. 0~9의 정수와 연산자 +-x으로 이루어짐
연산자 우선순위는 모두 동일해 수식 계산할 때는 왼쪽부터 순서대로 계산해야한다.

수식에 괄호를 추가하면, 괄호 안 식을 먼저 계산해야 한다. 
    1. 괄호 안에는 연산자가 하나만 들어 있어야 한다.
    2. 중첩된 괄호는 사용할 수 없다. 

수식이 주어졌을 때, 괄호를 적절히 추가해 만들 수 있는 식의 결과의 최댓값을 구하는 프로그램을 작성하자.
괄호 개수의 제한은 없으며, 추가하지 않아도 된다.
'''
N = int(input())
arr = input()
num = list()
op = list()
for i in range(N):
    if i % 2 == 0:
        num.append(int(arr[i]))
    else:
        op.append(arr[i])
answer = -float('inf')

def cal(n1, op, n2):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    else:
        return n1 * n2


def dfs(current, idx):
    global answer
    if idx >= len(op):
        answer = max(current, answer)
        return
    # 1. 괄호 없이 다음 값을 더함
    tmp = cal(current, op[idx], num[idx+1])
    dfs(tmp, idx+1)

    # 2. 괄호를 만들어 넘김
    if idx + 1 < len(op):
        paren = cal(num[idx+1], op[idx+1], num[idx+2])
        tmp = cal(current, op[idx], paren)
        dfs(tmp, idx+2)

def main():
    dfs(num[0], 0)
    print(answer)

if __name__ == "__main__":
    main()

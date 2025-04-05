import sys
from itertools import permutations

try:
    sys.stdin = open("example3.txt", "r")
except FileNotFoundError:
    pass
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
cmd = list(map(int, input().split()))
cmd_list = list()
for idx, cnt in enumerate(cmd):
    cmd_list += [idx] * cnt


def main():
    max_answer = float('inf') * -1
    min_answer = float('inf')
    for operator_list in permutations(cmd_list, N - 1):
        tmp = arr[0]
        for idx, op in enumerate(operator_list):
            if op == 0:  # 덧셈
                tmp += arr[idx + 1]
            elif op == 1:  # 뺄셈
                tmp -= arr[idx + 1]
            elif op == 2:  # 곱셉
                tmp *= arr[idx + 1]
            else:  # 나눗셈
                if tmp < 0:
                    tmp = abs(tmp) // arr[idx + 1] * -1
                else:
                    tmp //= arr[idx + 1]

        max_answer = max(max_answer, tmp)
        min_answer = min(min_answer, tmp)
    print(max_answer)
    print(min_answer)


if __name__ == "__main__":
    main()

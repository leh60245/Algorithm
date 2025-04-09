import sys
from collections import deque

DEBUG = False
try:
    sys.stdin = open("example5.txt", "r")
    DEBUG = True
    print()
except FileNotFoundError:
    pass
input = sys.stdin.readline
'''
반지름 1~N 원판이 쌓여있음.
원판 반지름이 i라면, 그 원판을 i번째 원판이라 함.
각각 원판에는 M개 정수 적혀있고, i번째 원판에 적힌 j번째 수의 위치는 (i, j)로 표현한다.

[인접한 수 위치]
1. (i, 1)은 (i, 2), (i, M)과 인접
   (i, M)은 (i, M-1), (i, 1)과 인접
   (i, j)는 (i, j-1), (i, j+1)과 인접 (2<= j <= M-1)
2. (1, j)는 (2,j)와 인접
   (N, j)는 (N-1, j)와 인접
   (i, j)는 (i-1, j), (i+1, j)와 인접 (2 <= i <= N-1)
   
[회전-조건]
원판 회전은 독립적으로 이루어짐. 2번 원판을 회전했을 대, 나머지 원판은 회전하지 않는다.
원판 회전할 때는 수의 위치를 기준으로 하며, 회전시킨 후의 수의 위치는 회전시키기 전과 일치해야 한다.

[회전-방법] 총 T번, 회전 방법은 이미 정해짐, i번째 회전할때 사용하는 변수는 xi, di, ki이다.
1. 번호가 xi의 배수인 원판을 di방향으로 ki칸 회전시킨다. 
    di= (0: 시계), (1: 반시계)
2. 원판에 수가 남아 있으면 -> 인접한 수가 같은 것을 모두 찾는다.
    1) 그러한 수가 있는 경우: 원판에서 인접하면서 같은 수를 모두 지운다.
    2) 없는 경우: (1) 모든 원판에 적힌 수의 평균을 구하고, (2) 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.

[목표] 원판을 T번 회전시킨 후 원판에 적힌 수의 합을 구하자.
[제한]
2 ≤ N, M ≤ 50
1 ≤ T ≤ 50
1 ≤ 원판에 적힌 수 ≤ 1,000
2 ≤ xi ≤ N
0 ≤ di ≤ 1
1 ≤ ki < M
'''
N, M, T = map(int, input().split())
disk_list = list()
for i in range(N):
    disk_list.append(deque(list(map(int, input().split()))))
cmd_list = list()
for _ in range(T):
    cmd_list.append(tuple(map(int, input().split())))


def rotate_disk(si, d, k):
    direct = 1 if d == 0 else -1
    for _ in range(k):
        disk_list[si].rotate(direct)


def avg_disk():
    ans = 0
    cnt = 0
    for disk in disk_list:
        for v in disk:
            if v != 0:
                ans += v
                cnt += 1

    if cnt == 0:
        return False
    return ans / cnt


def find_disk():
    change_list = set()
    for si in range(N):
        for j in range(M):
            if disk_list[si][j] == 0:
                continue
            tmp = disk_list[si][j]
            # disk 내부 인접
            left_j, right_j = (j - 1, j + 1) if j < M - 1 else (j - 1, 0)
            if tmp == disk_list[si][left_j]:
                change_list.add((si, j))
                change_list.add((si, left_j))
            if tmp == disk_list[si][right_j]:
                change_list.add((si, j))
                change_list.add((si, right_j))
            # disk 간 인접
            if si > 0:
                if tmp == disk_list[si - 1][j]:
                    change_list.add((si, j))
                    change_list.add((si - 1, j))
            if si < N - 1:
                if tmp == disk_list[si + 1][j]:
                    change_list.add((si, j))
                    change_list.add((si + 1, j))
    return change_list


def clean_disk(change_list):
    for i, j in change_list:
        disk_list[i][j] = 0
    if len(change_list) != 0:
        return False

    avg = avg_disk()
    if not avg:
        return True

    for i, disk in enumerate(disk_list):
        for j, v in enumerate(disk):
            if v == 0:
                continue
            if v > avg:
                disk_list[i][j] = v - 1
            elif v < avg:
                disk_list[i][j] = v + 1
    return False

def visual(grid):
    for disk in disk_list:
        for v in disk:
            if v == 0:
                print("x", end=" ")
            else:
                print(v, end=" ")
        print()


def main():
    for t, cmd in enumerate(cmd_list):
        if DEBUG:
            print(f"============ time {t} =============")
        x, d, k = cmd
        rotated_disk_index = list()
        for disk_index in range(x, N + 1, x):
            disk_index -= 1
            rotated_disk_index.append(disk_index)
            rotate_disk(disk_index, d, k)
        if DEBUG:
            print("rotate")
            visual(disk_list)

        change_list = find_disk()
        is_end = clean_disk(change_list)

        if DEBUG:
            print("clean")
            visual(disk_list)

        if is_end:
            print(0)
            return

    answer = 0
    for disk in disk_list:
        answer += sum(disk)

    print(answer)


if __name__ == "__main__":
    main()

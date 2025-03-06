import sys

try:
    sys.stdin = open("input7.txt", "r")
except FileNotFoundError:
    pass

input = sys.stdin.readline

# 틀린 제출 1회 = 턱걸이 5회
# 계란으로 계란을 치기로 함
# 계란마다 '내구도' & '모게
# 계란으로 계란을 치면 각 계란의 내구도는 상대 계란의 무게만큼 깎임
# 내구도가 0 이하가 되면 깨짐
# 일렬로 놓인 계란에 대해 왼쪽부터 차례로 들어서 '한 번씩만' 다른 계란을 침
# 최종적으로 '최대한 많은 계란'을 깨는 문제
# 과정
# 1. 가장 왼쪽 계란을 든다.
# 2. 손의 계란으로 '깨지지 않은' 다른 계란 중 하나를 친다.
#    단, 손에 든 계란이 깨졌거나, 깨지지 않은 다른 계란이 없으면 치지 않고 넘어간다.
#    이후, 손에 든 계란을 원래 자리에 내려 놓고 3번 과정을 진행한다.
# 3. 가장 최근에 든 계란의 한 칸 오른쪽 계란을 손에 들고 2번 과정을 다시 진행한다.
#    단, 가장 최근에 든 계란이 가장 오른쪽에 위치한 경우, 계란을 치는 과정을 '종료한다'.
#
# 최대 몇 개의 계란을 깰 수 있는지 알아보자.

N = int(input())  # 계란 수
eggs_hp = []
eggs_weight = []
for _ in range(N):
    h, w = map(int, input().split())
    eggs_hp.append(h)
    eggs_weight.append(w)
max_broken = 0


def backtracking(hp, start):
    global max_broken
    if start == N:
        max_broken = max(max_broken, hp.count(0))
        return
    if hp[start] == 0:
        backtracking(hp, start + 1)
    else:  # hp[start] != 0
        for i in range(N):
            if i == start:
                continue
            tmp_hp = [i for i in hp]
            if hp[i] == 0:
                backtracking(tmp_hp, start + 1)
            else:
                tmp_hp[start] = max(tmp_hp[start] - eggs_weight[i], 0)
                tmp_hp[i] = max(tmp_hp[i] - eggs_weight[start], 0)
                backtracking(tmp_hp, start + 1)


def main():
    backtracking(eggs_hp, 0)
    print(max_broken)


if __name__ == "__main__":
    main()

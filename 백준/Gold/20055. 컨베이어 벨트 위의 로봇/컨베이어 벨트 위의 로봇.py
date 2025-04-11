import sys
from collections import deque


DEBUG = False
try:
    sys.stdin = open("example4.txt", "r")
    DEBUG = True
    print()
except FileNotFoundError:
    pass
input = sys.stdin.readline
'''
2N개의 칸이 회전 시계 방향으로 회전
i번 칸 내구도는 Ai
1번 칸이 올리는 위치, N번 칸이 내리는 위치

박스 모양 로봇을 하나씩 올리려고 함. 로봇은 올리는 위치에만 올릴 수 있음
언제든 로봇이 내리는 위치에 도달하면 즉시 내림
로봇은 컨베이어 벨트 위에서 스스로 이동할 수 있음. 
로봇을 올리는 위치에 올리거나 로봇이 어떤 칸으로 이동시 그 칸의 내구도는 즉시 1 감소

벨트를 이용해 로봇들을 건너편으로 옮기려 함. 로봇을 옮기는 과정은 아래와 같음
1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다. 
2. 가장 먼저 벨트 위의 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있으면 간다. 
    1) 만약, 이동할 수 없으면 가만히 있는다.
    2) 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸 내구도가 1 이상 남아야 함
3. 올리는 위치에 있는 칸 내구도가 0이 아니라면 로봇을 올림
4. 내구도가 0인 칸의 개수가 K개 이상이면 과정을 종료한다. 아니면 1로 돌아간다.

[목표] 종료되었을 때, 몇 번째 단계가 진행중이었는지 구하자. 가장 처음 수행되는 단계가 1째 단계
'''
N, K = map(int, input().split())
life = deque(list(map(int, input().split())))  # 1이 오른쪽 회전
robot = [] # 어느 위치에 있는지 저장. 가장 늦게 들어온 로봇이 리스트 앞에 있음 (칸 번호 X)
def damage(idx):
    global life
    life[idx] -= 1

def check_life():
    cnt = 0
    for v in life:
        if v == 0:
            cnt += 1
    if cnt >= K:
        return True
    return False

def visual_life_robot(label = "DEBUG"):
    if not DEBUG:
        return
    print(f"{label}")
    print(*life)
    line = [0 for _ in range(N)]
    for v in robot:
        line[v] += v
    print(*line)
    return

def main():
    global robot
    t = 1
    while True:
        if DEBUG:
            print(f"========== time {t} ===============")
        # 회전하기: 칸은 이동, robot은 위치 증가.
        life.rotate(1)
        new_robot = []
        for v in robot:
            v += 1
            if v == N-1:    # 즉시 내리기
                continue
            new_robot.append(v)
        robot = new_robot
        visual_life_robot("rotate")
        # 로봇 이동하기. i는 robot의 순서, v는 0~N-2 안의 위치
        new_robot = []
        for i, v in enumerate(robot):
            # 바로 앞에 로봇이 있는가?
            if i > 0 and new_robot and new_robot[-1] == v+1:
                new_robot.append(v)
                continue
            # 바로 앞 칸의 내구도가 1 이상인가?
            if life[v+1] == 0:
                new_robot.append(v)
                continue
            v += 1 # 이동한다.
            damage(v) # 로봇이 이동하면 내구도 감소
            if v == N-1: # 바로 내리기
                continue
            new_robot.append(v)
        robot = new_robot
        visual_life_robot("move robot")
        # 로봇 올리기
        if life[0] >= 1:
            robot.append(0)
            damage(0)
        visual_life_robot("on the line")
        if check_life():
            print(t)
            return

        t += 1



if __name__ == "__main__":
    main()

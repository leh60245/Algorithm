# 1 = 가위, 2 = 바위, 3 = 보
BEATS = {1: 3, 2: 1, 3: 2}          # x 가 이기는 상대
NAME  = {1: "가위", 2: "바위", 3: "보"}

def step(points, state):
    new = state[:]                   # 동시 갱신이므로 반드시 복사본에 쓴다
    for a in range(len(points)):
        b = points[a]
        if BEATS[state[a]] == state[b]:
            new[b] = state[a]
    return new

def show(t, state):
    print(f"  t={t}: {[NAME[s] for s in state]}")

# --- 실험 A: 나를 겨냥한 사람이 여럿이면 충돌이 날까? ---
print("[실험 A] 0,1,2 가 모두 3번을 겨냥. 3번은 '보'.")
points = [3, 3, 3, 3]
for combo in [[1,1,1,3], [1,2,1,3], [2,2,2,3]]:
    winners = [NAME[combo[a]] for a in range(3) if BEATS[combo[a]] == combo[3]]
    print(f"  겨냥하는 상태 {[NAME[c] for c in combo[:3]]} -> 실제로 이기는 사람들: {winners}")
print("  => 어떤 상태를 이기는 상태는 딱 하나뿐이라, 이기는 사람들끼리는 항상 같은 상태. 충돌 불가.\n")

# --- 실험 B: 시간이 지나면 정말 안정되나? ---
print("[실험 B] 0->1->2->0 사이클, 초기 [가위, 보, 바위]")
points = [1, 2, 0]
state  = [1, 3, 2]
seen = {}
t = 0
while tuple(state) not in seen:
    seen[tuple(state)] = t
    show(t, state)
    state = step(points, state)
    t += 1
start = seen[tuple(state)]
print(f"  t={t} 에서 t={start} 상태로 되돌아옴 -> 꼬리 {start}, 주기 {t - start}")

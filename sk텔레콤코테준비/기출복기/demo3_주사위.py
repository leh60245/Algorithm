from functools import lru_cache
import itertools

def best_with_reset(n, dice):
    """자발적 리셋(주사위를 소모하지 않음)을 허용했을 때 도달한 최대 위치"""
    M = n + 1
    best = 0
    # (주사위 인덱스, 현재 실제 위치) 를 전부 탐색 (작은 케이스용 브루트포스)
    stack = [(0, 0)]
    seen = set()
    while stack:
        i, pos = stack.pop()
        if (i, pos) in seen:
            continue
        seen.add((i, pos))
        best = max(best, pos)
        if i == len(dice):
            continue
        d = dice[i]
        for start in (pos, 0):              # 그대로 굴리기 / 리셋하고 굴리기
            nxt = start + d
            if nxt % M == 0:                # 위험 구역을 밟음
                nxt = 0
            stack.append((i + 1, nxt))
    return best

def best_no_reset(n, dice):
    M = n + 1
    pos, best = 0, 0
    for d in dice:
        pos += d
        if pos % M == 0:
            pos = 0
        best = max(best, pos)
    return best

print("[실험 C] 리셋을 안 쓰면 손해 보는 경우 찾기 (n, 주사위) 완전탐색")
found = 0
for n in range(1, 5):
    for L in range(1, 5):
        for dice in itertools.product(range(1, 7), repeat=L):
            a, b = best_with_reset(n, list(dice)), best_no_reset(n, list(dice))
            if a > b and found < 4:
                M = n + 1
                print(f"  n={n} (위험구역 {M},{2*M},{3*M}...), 주사위={list(dice)}"
                      f"  -> 리셋 없이 {b}, 리셋 쓰면 {a}")
                found += 1

print("\n[실험 D] n=3(위험구역 4,8,12...), 주사위=[2,2,5] 손으로 따라가기")
print("  리셋 X : 0 -(2)-> 2 -(2)-> 4(위험!)->0 -(5)-> 5      최대 5")
print("  리셋 O : 0 -(2)-> 2 [리셋] 0 -(2)-> 2 -(5)-> 7       최대 7")
print(f"  코드 확인 -> 리셋X={best_no_reset(3,[2,2,5])}, 리셋O={best_with_reset(3,[2,2,5])}")

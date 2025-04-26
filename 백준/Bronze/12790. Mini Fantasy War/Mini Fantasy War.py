# 테스트 케이스 수 입력
T = int(input())

for _ in range(T):
    # 기본 능력치 4개 + 장비 변화량 4개 입력
    base_hp, base_mp, base_attack, base_defense, delta_hp, delta_mp, delta_attack, delta_defense = map(int, input().split())
    
    # 최종 능력치 계산
    final_hp = base_hp + delta_hp
    final_mp = base_mp + delta_mp
    final_attack = base_attack + delta_attack
    final_defense = base_defense + delta_defense

    # 조건 처리
    if final_hp < 1:
        final_hp = 1
    if final_mp < 1:
        final_mp = 1
    if final_attack < 0:
        final_attack = 0

    # 최종 전투력 계산
    combat_power = (1 * final_hp) + (5 * final_mp) + (2 * final_attack) + (2 * final_defense)

    # 결과 출력
    print(combat_power)

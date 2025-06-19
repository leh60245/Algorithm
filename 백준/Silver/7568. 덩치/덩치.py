N = int(input())  # 사람 수 입력
people = [tuple(map(int, input().split())) for _ in range(N)]  # (몸무게, 키) 저장

ranks = []  # 각 사람의 등수를 저장할 리스트

for i in range(N):
    rank = 1  # 기본 등수는 1등
    for j in range(N):
        if i == j:
            continue  # 자기 자신은 비교하지 않음
        # 상대가 몸무게도 크고 키도 크면
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            rank += 1  # 나보다 큰 덩치이므로 등수 하나 밀림
    ranks.append(rank)

print(' '.join(map(str, ranks)))  # 결과 출력

# 국가 수 N, 등수를 알고 싶은 국가 번호 K
N, K = map(int, input().split())

countries = []

# 국가 번호, 금, 은, 동 입력받아 리스트에 저장
for _ in range(N):
    num, gold, silver, bronze = map(int, input().split())
    countries.append((num, gold, silver, bronze))

# 금 > 은 > 동 기준으로 내림차순 정렬
countries.sort(key=lambda x: (-x[1], -x[2], -x[3]))

rank = 1  # 현재 등수
prev_medal = countries[0][1:]  # 첫 나라의 메달 정보
rank_dict = {countries[0][0]: 1}  # 국가 번호: 등수

for i in range(1, N):
    # 현재 나라 메달 정보
    curr = countries[i][1:]
    
    # 이전 나라와 메달 수 같으면 동일 등수
    if curr == prev_medal:
        rank_dict[countries[i][0]] = rank
    else:
        # 메달 다르면 현재 인덱스 +1이 등수
        rank = i + 1
        rank_dict[countries[i][0]] = rank
        prev_medal = curr

# K번 국가의 등수 출력
print(rank_dict[K])

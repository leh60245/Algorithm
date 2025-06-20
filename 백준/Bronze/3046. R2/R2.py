# R1과 S를 입력받는다
R1, S = map(int, input().split())

# 평균 S로부터 R2를 역산한다
R2 = 2 * S - R1

# 결과 출력
print(R2)

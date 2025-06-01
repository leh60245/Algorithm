# 현재 시, 분, 초를 입력받음
A, B, C = map(int, input().split())

# 요리 시간(초)을 입력받음
D = int(input())

# 현재 시간을 초로 변환
current_time = A * 3600 + B * 60 + C

# 요리 시간(초)을 더함
end_time = current_time + D

# 종료 시간을 시, 분, 초로 다시 나눔
hour = (end_time // 3600) % 24  # 24시간을 넘어가면 나머지로 순환
minute = (end_time % 3600) // 60
second = end_time % 60

# 결과 출력
print(hour, minute, second)

HH, MM = map(int, input().split())

start_minutes = 9 * 60           # 시작 시간: 9:00 AM
submit_minutes = HH * 60 + MM    # 제출 시간

elapsed = submit_minutes - start_minutes  # 경과 시간 (분)

print(elapsed)

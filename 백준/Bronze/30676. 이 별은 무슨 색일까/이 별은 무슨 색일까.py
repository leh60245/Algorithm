# 파장을 입력받습니다
wavelength = int(input())

# 조건문으로 범위 확인 후 색상 출력
if 620 <= wavelength <= 780:
    print("Red")  # 빨간색
elif 590 <= wavelength < 620:
    print("Orange")  # 주황색
elif 570 <= wavelength < 590:
    print("Yellow")  # 노란색
elif 495 <= wavelength < 570:
    print("Green")  # 초록색
elif 450 <= wavelength < 495:
    print("Blue")  # 파란색
elif 425 <= wavelength < 450:
    print("Indigo")  # 남색
elif 380 <= wavelength < 425:
    print("Violet")  # 보라색

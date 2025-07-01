T = int(input())  # 학기 수

for _ in range(T):
    N = int(input())  # 과목 수
    total_credits = 0
    total_grade_points = 0.0
    for _ in range(N):
        C, G = input().split()
        C = int(C)
        G = float(G)
        total_credits += C
        total_grade_points += C * G
    GPA = total_grade_points / total_credits
    print(total_credits, f"{GPA:.1f}")

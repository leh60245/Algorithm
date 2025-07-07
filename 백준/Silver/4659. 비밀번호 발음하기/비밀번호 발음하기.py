vowel = ['a', 'e', 'i', 'o', 'u']

def is_acceptable(pw):
    has_vowel = False
    prev = ''           # 이전 문자
    vowel_streak = 0    # 모음 연속 횟수
    cons_streak = 0     # 자음 연속 횟수

    for i, ch in enumerate(pw):
        if ch in vowel:
            has_vowel = True
            vowel_streak += 1
            cons_streak = 0
        else:
            cons_streak += 1
            vowel_streak = 0

        # 모음 3연속 or 자음 3연속
        if vowel_streak >= 3 or cons_streak >= 3:
            return False

        # 같은 글자 2연속 (ee, oo는 예외)
        if i > 0 and pw[i] == prev and pw[i] not in ['e', 'o']:
            return False

        prev = ch

    # 반드시 모음이 1개 이상 포함되어야 함
    if not has_vowel:
        return False

    return True

while True:
    pw = input()
    if pw == "end":
        break
    if is_acceptable(pw):
        print(f"<{pw}> is acceptable.")
    else:
        print(f"<{pw}> is not acceptable.")

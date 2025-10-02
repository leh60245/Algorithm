# import sys
# sys.stdin = open("input.txt")

n = int(input())
board = list()
heart_i, heart_j = None, None
left_arm, right_arm, waist, left_leg, right_leg = None, None, None, None, None

for _ in range(n):
    board.append(list(map(str, input().strip())))


for i in range(n):
    for j in range(n):
        if board[i][j] == "*":
            heart_i, heart_j = i + 1, j
            break
    if (heart_i, heart_j) != (None, None):
        break

left_arm = board[heart_i][:heart_j].count("*")
right_arm = board[heart_i][heart_j+1:].count("*")

rotated_board = [[board[n-j-1][i] for j in range(n)] for i in range(n)]

waist = rotated_board[heart_j].count("*") - 2
left_leg = rotated_board[heart_j-1].count("*") - 1
right_leg = rotated_board[heart_j+1].count("*") - 1

print(heart_i + 1, heart_j + 1)
print(left_arm, right_arm, waist, left_leg, right_leg)
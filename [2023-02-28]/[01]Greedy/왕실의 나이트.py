import sys

# 상하좌우
# (상하, 좌우)
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2), (-1, -2), (1, 2), (-1, 2)]

input_data = sys.stdin.readline().rstrip()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    # 해당 위치로 이동 가능하다면 count++
    if (next_row >= 1) and (next_row <= 8) and (next_column >= 1) and (next_column <= 8):
        result += 1

print(result)


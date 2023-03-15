import sys

input = sys.stdin.readline

board = input().rstrip().split('.')

print(board)

for b in board:
    if len(b) % 2 != 0:
        print(-1)
        break


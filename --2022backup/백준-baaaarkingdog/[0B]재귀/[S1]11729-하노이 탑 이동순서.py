import sys

input = sys.stdin.readline

n = int(input().rstrip())
moves = []


def func(a, b, n):
    if n == 1:
        moves.append([a, b])
        return

    # 1) 다 이동
    func(a, 6 - a - b, n - 1)

    # 2) 나머지 1개 이동
    moves.append([a, b])

    # 3) b로 이동
    func(6 - a - b, b, n - 1)


func(1, 2, n)

print(len(moves))
for a, b in moves:
    print(a, b)

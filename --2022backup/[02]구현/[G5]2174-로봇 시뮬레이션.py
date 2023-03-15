A, B = map(int, input().split())
N, M = map(int, input().split())

# directions = {'S': 0, 'E': 1, 'N': 2, 'W': 3}
directions = {'W': 0, 'S': 1, 'E': 2, 'N': 3}

'''
    https://rebas.kr/739
'''

#       S  E  N  W
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# 좌하우상
#     W  S   E  N
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

# dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
w = [[0] * (A + 1) for _ in range(B + 1)]
r = [[0, 0, 0] for _ in range(N + 1)]


def solve(i, d, c):
    x, y, z = r[i]
    w[x][y] = 0
    for _ in range(c):
        if d == 'L':
            z = (z + 1) % 4
        elif d == 'R':
            z = (z + 3) % 4
        else:
            x, y = x + dx[z], y + dy[z]
            if x < 1 or x > B or y < 1 or y > A:
                print("Robot %d crashes into the wall" % i)
                return True
            if w[x][y]:
                print("Robot %d crashes into robot %d" % (i, w[x][y]))
                return True
    r[i] = x, y, z
    w[x][y] = i
    return False


for i in range(1, N + 1):
    x, y, z = input().split()
    w[int(y)][int(x)] = i
    r[i] = [int(y), int(x), directions[z]]

crash = False
for _ in range(M):
    i, d, c = input().split()
    if not crash:
        crash = solve(int(i), d, int(c))

if not crash:
    print("OK")

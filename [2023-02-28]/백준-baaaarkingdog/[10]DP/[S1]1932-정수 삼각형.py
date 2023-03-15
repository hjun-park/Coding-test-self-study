import sys

input = sys.stdin.readline

n = int(input().rstrip())
tri = []
for _ in range(n):
    tri.append(list(map(int, input().split())))

d = [[0] * (n + 2) for _ in range(n + 2)]


def logic():
    if n == 1:
        return tri[0][0]

    d[0][0] = tri[0][0]
    d[1][0] = tri[1][0] + d[0][0]
    d[1][1] = tri[1][1] + d[0][0]

    for i in range(2, n):
        for j in range(i + 1):
            d[i][j] = tri[i][j] + max(d[i - 1][j - 1], d[i - 1][j])

    return max(d[n - 1])


print(logic())

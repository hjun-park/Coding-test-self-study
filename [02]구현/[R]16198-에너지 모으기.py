import sys

input = sys.stdin.readline

N = int(input())
w = list(map(int, input().split()))
result = 0


def logic(s):
    global result

    if len(w) == 2:
        if s > result:
            result = s
        return

    for i in range(1, len(w) - 1):
        energy = w[i - 1] * w[i + 1]
        temp = w[i]
        del w[i]
        logic(s + energy)
        w.insert(i, temp)


logic(0)
print(result)

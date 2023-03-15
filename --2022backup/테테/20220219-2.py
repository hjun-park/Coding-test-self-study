import sys

input = sys.stdin.readline


def logic(bricks):
    h = max(bricks)
    w = len(bricks)
    result = 0

    for i in range(1, w - 1):
        lx = max(bricks[:i])
        rx = max(bricks[i + 1:])

        comp = min(lx, rx)

        if bricks[i] < comp:
            result += comp - bricks[i]

    return result


br = [0, 2, 0, 1, 3, 1, 2, 0, 1, 0, 2, 0]
print(type(br))
print(logic(br))


br = [1, 2, 3, 4, 5, 6, 7]
print(logic(br))

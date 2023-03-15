import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(set(list(map(int, input().split())))))

temp = []


def logic(start):
    if len(temp) == M:
        print(*temp)
        return

    for i in range(start, len(nums)):
        temp.append(nums[i])
        logic(i)
        temp.pop()


logic(0)

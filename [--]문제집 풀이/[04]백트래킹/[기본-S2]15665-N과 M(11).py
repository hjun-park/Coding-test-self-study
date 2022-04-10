import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(set(list(map(int, input().split())))))

temp = []


def logic():
    if M == len(temp):
        print(*temp)
        return

    for i in range(len(nums)):
        temp.append(nums[i])
        logic()
        temp.pop()


logic()

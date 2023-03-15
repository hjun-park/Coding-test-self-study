import sys

# 1. 입력(테스트케이스, 통나무 개수, 통나무 리스트)
t = int(input())

for _ in range(t):
    n = int(input())
    trees = [int(x) for x in input().split()]
    trees.sort()

    max_height = 0
    for i in range(2, n):
        max_height = max(max_height, abs(trees[i] - trees[i-2]))

    print(max_height)

